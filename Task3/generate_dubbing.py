import os
import asyncio
import argparse
import shutil
import subprocess
import sys

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip()

async def generate_edge_tts(text, output_path, voice="zh-CN-XiaoxiaoNeural"):
    import edge_tts
    print(f"[Edge-TTS] 使用声音: {voice}")
    print(f"[Edge-TTS] 正在生成音频 (无需GPU，速度快)...")
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)
    print(f"[Edge-TTS] 音频已保存: {output_path}")

def generate_cosyvoice_cpu(text, reference_audio, output_path, model_path="pretrained_models/CosyVoice-300M"):
    try:
        from cosyvoice.cli.cosyvoice import CosyVoice
        import torch

        print(f"[CosyVoice] 加载模型: {model_path}")
        print("[CosyVoice] 警告: CPU 运行速度极慢，可能需要数十分钟...")
        cosyvoice = CosyVoice(model_path)
        cosyvoice.model = cosyvoice.model.to(torch.device("cpu"))

        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        first_chunk = True
        for i, chunk in enumerate(cosyvoice.inference_zero_shot(text, reference_audio, "参考音频的文本转录内容")):
            if first_chunk:
                chunk.to_wav(output_path)
                first_chunk = False
                print(f"[CosyVoice] 已保存: {output_path}")
            else:
                temp_path = output_path.replace('.wav', f'_part{i}.wav')
                chunk.to_wav(temp_path)
                print(f"[CosyVoice] 已保存分段: {temp_path}")
        print("[CosyVoice] 生成完成!")
    except ImportError:
        print("[错误] CosyVoice 未安装。请运行:")
        print("  git clone https://github.com/FunAudioLLM/CosyVoice")
        print("  cd CosyVoice && pip install -r requirements.txt")
    except Exception as e:
        print(f"[CosyVoice 错误] {e}")

def run_moss_nano(text, reference_audio, output_path, moss_repo_dir="MOSS-TTS-Nano"):
    print("[MOSS-TTS-Nano] 0.1B 轻量模型，纯CPU实时运行，支持音色克隆")

    abs_repo = os.path.abspath(moss_repo_dir)
    abs_ref = os.path.abspath(reference_audio)

    # 准备环境变量
    env = os.environ.copy()
    pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = abs_repo + (os.pathsep + pythonpath if pythonpath else "")
    env["HF_ENDPOINT"] = "https://hf-mirror.com"

    # 1. 尝试使用已安装的 CLI
    cli_cmd = ["moss-tts-nano", "generate", "--prompt-speech", abs_ref, "--text", text]
    try:
        result = subprocess.run(cli_cmd, capture_output=True, text=True, timeout=5, env=env)
        if result.returncode == 0:
            print("[MOSS-TTS-Nano] CLI 生成成功")
            return
    except FileNotFoundError:
        pass
    except Exception:
        pass

    # 2. 尝试调用仓库里的 infer.py
    infer_script = os.path.join(abs_repo, "infer.py")
    if os.path.exists(infer_script):
        print(f"[MOSS-TTS-Nano] 使用仓库脚本: {infer_script}")
        # 文本过长时截断到约100字，避免CPU运行过久
        short_text = text[:100] if len(text) > 100 else text
        if len(text) > 100:
            print(f"[MOSS-TTS-Nano] 文本较长({len(text)}字)，首次运行截断为100字以测试")
        cmd = [
            sys.executable, infer_script,
            "--prompt-audio-path", abs_ref,
            "--text", short_text,
            "--device", "cpu"
        ]
        print(f"[MOSS-TTS-Nano] 运行: {' '.join(cmd)}")
        print("[MOSS-TTS-Nano] 首次运行需从 HuggingFace 下载模型(约数百MB)，请耐心等待...")
        result = subprocess.run(cmd, env=env)
        if result.returncode == 0:
            default_output = os.path.join(abs_repo, "generated_audio", "infer_output.wav")
            if os.path.exists(default_output):
                os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
                shutil.copy2(default_output, output_path)
                print(f"[MOSS-TTS-Nano] 音频已复制到: {output_path}")
            else:
                print(f"[MOSS-TTS-Nano] 生成完成，默认输出位置: {default_output}")
            return
        else:
            print("[MOSS-TTS-Nano] infer.py 运行失败")
            return

    # 3. 尝试直接 Python API（如果 pip install -e . 已执行）
    try:
        from modeling_moss_tts_nano import MossTTSNanoForCausalLM
        from configuration_moss_tts_nano import MossTTSNanoConfig
        print("[MOSS-TTS-Nano] 使用 Python API 直接推理...")

        config = MossTTSNanoConfig.from_pretrained(".")
        model = MossTTSNanoForCausalLM.from_pretrained(".", config=config)
        result = model.inference(
            text=text,
            output_audio_path=output_path,
            mode="continuation"
        )
        print(f"[MOSS-TTS-Nano] 音频已保存: {output_path}")
        return
    except ImportError:
        pass
    except Exception as e:
        print(f"[MOSS-TTS-Nano] Python API 调用失败: {e}")

    # 4. 全部失败，给出安装提示
    print("\n[错误] MOSS-TTS-Nano 未找到。请按以下步骤安装:")
    print("  1. 下载仓库 (无git可直接下载zip):")
    print("     https://github.com/OpenMOSS/MOSS-TTS-Nano/archive/refs/heads/main.zip")
    print("  2. 解压后将文件夹重命名为 'MOSS-TTS-Nano' 并放在本脚本同级目录")
    print("  3. 安装依赖:")
    print("     cd MOSS-TTS-Nano")
    print("     pip install -r requirements.txt")
    print("     pip install -e .")
    print("  4. 重新运行本脚本")

def main():
    parser = argparse.ArgumentParser(description="生成 CS25 中文配音音频")
    parser.add_argument("--text", default="sample_500.txt", help="输入文本文件路径")
    parser.add_argument("--reference", default="ref_01.wav", help="参考音频路径 (用于音色克隆)")
    parser.add_argument("--output", default="output/dubbing.mp3", help="输出音频路径")
    parser.add_argument("--mode", default="edge", choices=["edge", "clone", "moss"],
                        help="生成模式: edge(快速) / clone(CosyVoice音色克隆) / moss(MOSS-TTS-Nano轻量克隆)")
    parser.add_argument("--voice", default="zh-CN-XiaoxiaoNeural", help="Edge-TTS 声音名称")
    parser.add_argument("--moss-repo", default="MOSS-TTS-Nano-main", help="MOSS-TTS-Nano 仓库目录路径")
    args = parser.parse_args()

    if not os.path.exists(args.text):
        print(f"[错误] 文本文件不存在: {args.text}")
        return

    text = load_text(args.text)
    print(f"[信息] 输入文本长度: {len(text)} 字符")

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)

    if args.mode == "edge":
        print("[信息] 使用 Edge-TTS 模式: 无需GPU，声音清晰，但无法完全克隆参考音色")
        asyncio.run(generate_edge_tts(text, args.output, voice=args.voice))
    elif args.mode == "clone":
        if not os.path.exists(args.reference):
            print(f"[错误] 参考音频不存在: {args.reference}")
            return
        print("[信息] 使用 CosyVoice 音色克隆模式: 尝试模仿参考音色 (CPU运行极慢)")
        output_wav = args.output.replace(".mp3", ".wav") if args.output.endswith(".mp3") else args.output
        generate_cosyvoice_cpu(text, args.reference, output_wav)
    elif args.mode == "moss":
        if not os.path.exists(args.reference):
            print(f"[错误] 参考音频不存在: {args.reference}")
            return
        print("[信息] 使用 MOSS-TTS-Nano 轻量克隆模式: 0.1B参数，纯CPU实时，支持音色克隆")
        run_moss_nano(text, args.reference, args.output, moss_repo_dir=args.moss_repo)

if __name__ == "__main__":
    main()
