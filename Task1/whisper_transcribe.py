import whisper
import os
import time
from pathlib import Path

def format_timestamp(seconds):
    """将秒数转换为 [HH:MM:SS] 格式"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def format_duration(seconds):
    """将秒数转换为可读的时长格式"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours}小时{minutes}分钟{secs}秒"
    elif minutes > 0:
        return f"{minutes}分钟{secs}秒"
    else:
        return f"{secs}秒"

def transcribe_audio(input_audio_path, output_md_path, model_name="large-v3"):
    """
    使用 Whisper 模型转录音频并生成带时间戳的 Markdown 文件
    
    参数:
        input_audio_path: 输入音频文件路径 (.mp3 / .wav / .m4a)
        output_md_path: 输出 Markdown 文件路径
        model_name: Whisper 模型名称
            - large-v3: 约2.9GB显存 (FP16)，精度最高
            - medium: 约5GB显存需求
            - small: 约2GB显存
            - base: 约1GB显存
            - tiny: 约0.5GB显存
    """
    print(f"[1/3] 加载 Whisper 模型: {model_name}")
    load_start = time.time()
    model = whisper.load_model(model_name)
    print(f"      模型加载完成 (耗时 {time.time() - load_start:.1f}s)")
    
    print(f"[2/3] 正在转录音频: {input_audio_path}")
    transcribe_start = time.time()
    result = model.transcribe(
        input_audio_path,
        language="en",
        task="transcribe",
        verbose=True
    )
    print(f"      转录完成 (耗时 {time.time() - transcribe_start:.1f}s)")
    
    # 获取音频文件名作为标题
    audio_name = Path(input_audio_path).stem
    
    print(f"[3/3] 写入输出文件: {output_md_path}")
    os.makedirs(os.path.dirname(output_md_path) if os.path.dirname(output_md_path) else ".", exist_ok=True)
    
    with open(output_md_path, 'w', encoding='utf-8') as f:
        # 标题
        f.write(f"# CS25 Lecture 1: {audio_name} - 原始转录文本\n\n")
        
        # 音频信息
        f.write("## 音频信息\n\n")
        f.write(f"- 来源：Stanford CS25 Transformers United V6\n")
        f.write(f"- 时长：{format_duration(result['segments'][-1]['end'])}\n")
        f.write(f"- 模型：{model_name}\n")
        f.write(f"- 总片段数：{len(result['segments'])}\n\n")
        
        # 完整文本（带时间戳）
        f.write("## 完整文本（带时间戳）\n\n")
        
        for segment in result["segments"]:
            start_time = format_timestamp(segment["start"])
            text = segment["text"].strip()
            f.write(f"[{start_time}] {text}\n\n")
    
    total_time = time.time() - load_start
    print(f"\n✓ 转录完成！")
    print(f"  总片段数: {len(result['segments'])}")
    print(f"  音频时长: {format_duration(result['segments'][-1]['end'])}")
    print(f"  总耗时: {total_time:.1f}s")
    print(f"  输出文件: {output_md_path}")
    
    return result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Whisper Audio Transcription for CS25 Lecture")
    parser.add_argument("--input", required=True, help="Input audio file path (.mp3/.wav/.m4a)")
    parser.add_argument("--output", default="output/lecture1_raw.md", help="Output markdown file path")
    parser.add_argument("--model", default="medium", choices=["tiny", "small", "medium", "large", "large-v3"], 
                        help="Whisper model size")
    args = parser.parse_args()
    
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    transcribe_audio(args.input, args.output, args.model)