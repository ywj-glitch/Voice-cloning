import os
import argparse
import subprocess
import sys

def check_cuda():
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False

def get_device():
    return "cuda" if check_cuda() else "cpu"

def load_script(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
        start_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('---'):
                start_idx = i + 1
                break
        return ''.join(lines[start_idx:]).strip()

def run_cosyvoice(script_text, reference_audio, output_path, model_path="pretrained_models/CosyVoice-300M", device=None):
    if device is None:
        device = get_device()
    try:
        from cosyvoice.cli.cosyvoice import CosyVoice
        import torch

        print(f"[Device] Using: {device}")
        print(f"Loading CosyVoice model from: {model_path}")
        cosyvoice = CosyVoice(model_path)

        if device == "cpu":
            cosyvoice.model = cosyvoice.model.to(torch.device("cpu"))
            print("Warning: Running on CPU will be very slow.")

        print("Starting voice cloning inference...")
        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)

        first_chunk = True
        for i, chunk in enumerate(cosyvoice.inference_zero_shot(
            script_text,
            reference_audio,
            "参考音频的文本转录内容"
        )):
            if first_chunk:
                chunk.to_wav(output_path)
                first_chunk = False
                print(f"Saved first chunk to: {output_path}")
            else:
                temp_path = output_path.replace('.wav', f'_part{i}.wav')
                chunk.to_wav(temp_path)
                print(f"Saved chunk {i} to: {temp_path}")

        print("CosyVoice inference completed successfully!")

    except ImportError:
        print("Error: CosyVoice module not found. Please install CosyVoice first.")
        print("Run: git clone https://github.com/FunAudioLLM/CosyVoice && cd CosyVoice && pip install -r requirements.txt")
    except Exception as e:
        print(f"Error during CosyVoice inference: {str(e)}")

def run_qwen_tts(script_text, reference_audio, output_path, model_name="Qwen/Qwen3-TTS-1.7B", device=None):
    if device is None:
        device = get_device()
    try:
        from transformers import AutoProcessor, AutoModel
        import torch

        print(f"[Device] Using: {device}")
        print(f"Loading Qwen3-TTS model: {model_name}")
        processor = AutoProcessor.from_pretrained(model_name)

        if device == "cpu":
            print("Warning: Running Qwen3-TTS on CPU requires ~8GB RAM and will be very slow.")
            model = AutoModel.from_pretrained(model_name, torch_dtype=torch.float32)
            model = model.to(torch.device("cpu"))
        else:
            model = AutoModel.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

        print("Processing text...")
        inputs = processor(text=script_text, return_tensors="pt")
        if device == "cpu":
            inputs = inputs.to(torch.device("cpu"))
        else:
            inputs = inputs.to(model.device)

        print("Generating audio...")
        with torch.no_grad():
            audio = model.generate(**inputs)

        print("Saving audio...")
        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)

        import soundfile as sf
        sf.write(output_path, audio.cpu().numpy()[0], samplerate=16000)

        print("Qwen3-TTS inference completed successfully!")

    except ImportError:
        print("Error: transformers or soundfile not installed.")
        print("Run: pip install transformers soundfile torch")
    except Exception as e:
        print(f"Error during Qwen3-TTS inference: {str(e)}")

def run_f5_tts(script_text, reference_audio, output_path, device=None):
    if device is None:
        device = get_device()
    try:
        print("Initializing F5-TTS...")
        if device == "cpu":
            print("Warning: F5-TTS on CPU is extremely slow and not recommended.")
        else:
            print("Note: F5-TTS requires ~16GB VRAM and manual setup.")
        print("Please refer to https://github.com/SamsungLabs/f5-tts for installation.")

    except Exception as e:
        print(f"Error during F5-TTS setup: {str(e)}")

def run_edge_tts(script_text, output_path, voice="zh-CN-XiaoxiaoNeural"):
    try:
        import edge_tts
        import asyncio

        print("[Device] Using Edge-TTS (online, no GPU/RAM required)")
        print(f"Selected voice: {voice}")
        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)

        async def generate():
            communicate = edge_tts.Communicate(script_text, voice)
            await communicate.save(output_path)

        asyncio.run(generate())
        print(f"Edge-TTS audio saved to: {output_path}")
        print("Note: Edge-TTS is an online service; voice cloning is not supported.")
        print("      It provides high-quality Chinese TTS without local model loading.")

    except ImportError:
        print("Error: edge-tts not installed.")
        print("Run: pip install edge-tts")
    except Exception as e:
        print(f"Error during Edge-TTS inference: {str(e)}")

def main():
    has_cuda = check_cuda()
    default_model = "cosyvoice" if has_cuda else "edge"

    parser = argparse.ArgumentParser(description="Voice Cloning TTS for CS25 Lecture Dubbing (CPU/GPU compatible)")
    parser.add_argument("--script", required=True, help="Path to voiceover script")
    parser.add_argument("--reference", default="", help="Path to reference audio (.wav) (required for cosyvoice/qwen3/f5)")
    parser.add_argument("--output", default="output/my_voice_dubbing.wav", help="Output audio path")
    parser.add_argument("--model", default=default_model,
                        choices=["cosyvoice", "qwen3", "f5", "edge"],
                        help="TTS model to use (default: edge for CPU-only, cosyvoice for GPU)")
    parser.add_argument("--model-path", default="pretrained_models/CosyVoice-300M",
                        help="Path to model files (for cosyvoice)")
    parser.add_argument("--device", default="auto", choices=["auto", "cpu", "cuda"],
                        help="Device to use (auto/cpu/cuda)")
    parser.add_argument("--voice", default="zh-CN-XiaoxiaoNeural",
                        help="Edge-TTS voice name (e.g. zh-CN-XiaoxiaoNeural, zh-CN-YunxiNeural)")
    args = parser.parse_args()

    if args.device == "auto":
        device = get_device()
    else:
        device = args.device

    print(f"Loading script from: {args.script}")
    script_text = load_script(args.script)
    print(f"Script length: {len(script_text)} characters")

    if args.model in ["cosyvoice", "qwen3", "f5"]:
        if not args.reference or not os.path.exists(args.reference):
            print(f"Error: --reference is required for model '{args.model}' and must exist.")
            return
        print(f"Using reference audio: {args.reference}")

    if args.model == "cosyvoice":
        run_cosyvoice(script_text, args.reference, args.output, args.model_path, device=device)
    elif args.model == "qwen3":
        run_qwen_tts(script_text, args.reference, args.output, device=device)
    elif args.model == "f5":
        run_f5_tts(script_text, args.reference, args.output, device=device)
    elif args.model == "edge":
        run_edge_tts(script_text, args.output, voice=args.voice)

if __name__ == "__main__":
    main()