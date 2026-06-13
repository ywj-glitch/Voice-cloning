"""
CS25 课程音频转录翻译与优化工具
使用 DeepSeek API 将英文转录文本翻译为学术化中文，并进行文字优化。
"""

import os
import re
import time
import argparse
from openai import OpenAI

# ============================================================
# 配置
# ============================================================
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"  # DeepSeek-V3

# 每个 chunk 大约覆盖的分钟数
CHUNK_MINUTES = 10

# ============================================================
# 解析原始转录文件
# ============================================================

def parse_raw_transcript(file_path):
    """解析 lecture1_raw.md，提取时间戳和文本段落"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配 [HH:MM:SS] 格式的时间戳
    pattern = r'^\[(\d{2}:\d{2}:\d{2})\]\s+(.+)$'
    segments = []
    
    # 跳过音频信息头部，从 "## 完整文本" 之后开始
    body_start = content.find("## 完整文本（带时间戳）")
    if body_start == -1:
        body_start = 0
    body = content[body_start:]

    for line in body.split('\n'):
        line = line.strip()
        if not line:
            continue
        match = re.match(pattern, line)
        if match:
            timestamp = match.group(1)
            text = match.group(2)
            segments.append((timestamp, text))

    return segments


def timestamp_to_seconds(ts):
    """将 HH:MM:SS 转为秒数"""
    parts = ts.split(':')
    return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])


def split_into_chunks(segments, chunk_minutes=CHUNK_MINUTES):
    """按时间窗口将段落分组"""
    chunk_seconds = chunk_minutes * 60
    chunks = []
    current_chunk = []
    chunk_start_sec = None

    for ts, text in segments:
        sec = timestamp_to_seconds(ts)
        if chunk_start_sec is None:
            chunk_start_sec = sec

        if sec - chunk_start_sec >= chunk_seconds and current_chunk:
            chunks.append(current_chunk)
            current_chunk = []
            chunk_start_sec = sec

        current_chunk.append((ts, text))

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def chunk_to_text(chunk):
    """将段落组转为 LLM 可处理的纯文本"""
    lines = []
    for ts, text in chunk:
        lines.append(f"[{ts}] {text}")
    return '\n'.join(lines)


# ============================================================
# DeepSeek API 调用
# ============================================================

SYSTEM_PROMPT = """你是一位专业的学术翻译与内容优化专家，擅长斯坦福大学计算机科学课程的本地化。

请将以下斯坦福大学 CS25 "Transformers United" 课程的英文转录文本翻译为中文，并进行学术化优化。

【翻译要求】
1. 术语标准化：使用国内AI/深度学习学术界通用译法：
   - Transformer → "Transformer架构"（首字母大写保留）
   - attention → "注意力机制"
   - self-attention → "自注意力机制"
   - token → "词元"（或保留"Token"）
   - embedding → "嵌入向量"
   - encoder/decoder → "编码器/解码器"
   - fine-tuning → "微调"
   - pre-training → "预训练"
   - inference → "推理"
   - prompt → "提示词"
   - BOS/EOS → "起始标记/结束标记"
   - RNN → "循环神经网络"
   - one-hot encoding → "独热编码"
   - softmax → "Softmax函数"
   - Word2Vec → "Word2Vec模型"
2. 学术风格：保持严谨、书面化的中文表达，如同斯坦福课堂讲义
3. 口语过滤：去除英文填充词（"um", "uh", "you know", "like", "kind of", "I guess"），但保留核心解释
4. 标注重点：对关键概念使用 **加粗**
5. 保留原始时间戳，格式转为 HTML 注释 `<!-- [HH:MM:SS] -->`

【输出格式】
请严格按照以下 Markdown 格式输出（不要用代码块包裹）：

## [根据内容提炼的小标题]

<!-- [HH:MM:SS] -->
翻译后的中文段落内容，**关键概念**加粗处理。

<!-- [HH:MM:SS] -->
下一个段落的中文翻译...

（继续直到所有段落翻译完毕）"""


def translate_chunk(client, chunk_text, chunk_index, total_chunks):
    """调用 DeepSeek API 翻译一个文本块"""
    user_prompt = f"以下是课程转录的第 {chunk_index + 1}/{total_chunks} 部分，请按要求翻译优化：\n\n{chunk_text}"

    print(f"  [{chunk_index + 1}/{total_chunks}] 发送翻译请求 (约 {len(chunk_text)} 字符)...")
    t_start = time.time()

    try:
        response = client.chat.completions.create(
            model=DEEPSEEK_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
            max_tokens=8192,
        )
        result = response.choices[0].message.content
        print(f"  [{chunk_index + 1}/{total_chunks}] 翻译完成 (耗时 {time.time() - t_start:.1f}s)")
        return result
    except Exception as e:
        print(f"  [{chunk_index + 1}/{total_chunks}] API 调用失败: {e}")
        raise


# ============================================================
# 输出生成
# ============================================================

def assemble_full_output(chunk_results, total_duration_str):
    """组装最终的中文 Markdown 文件"""
    lines = []
    lines.append("# CS25 第一讲：Transformer架构与大规模语言模型入门\n")
    lines.append("## 课程信息\n")
    lines.append(f"- 来源：Stanford CS25 Transformers United V6")
    lines.append(f"- 课程：CME 295 - Transformers and Large Language Models")
    lines.append(f"- 讲师：Afshin & Sherwin（双胞胎兄弟）")
    lines.append(f"- 时长：{total_duration_str}")
    lines.append(f"- 翻译引擎：DeepSeek-V3 (via API)")
    lines.append(f"- 处理方式：LLM 翻译 + 学术化优化\n")
    lines.append("---\n")
    lines.append("## 中文翻译（学术优化版）\n")

    for i, result in enumerate(chunk_results):
        lines.append(result.strip())
        lines.append("")

    return '\n'.join(lines)


def extract_voiceover_script(full_md_path, output_path, target_chars=1000):
    """从优化后的中文 Markdown 中提取配音脚本"""
    with open(full_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 移除所有 markdown 格式标记和时间戳注释，只保留纯中文文本
    cleaned = re.sub(r'<!-- \[.*?\] -->', '', content)
    cleaned = re.sub(r'#+\s+.*?\n', '', cleaned)
    cleaned = re.sub(r'\*\*', '', cleaned)
    cleaned = re.sub(r'\n+', '\n', cleaned)
    cleaned = re.sub(r'^\s*[-*]\s+.*?\n', '', cleaned, flags=re.MULTILINE)

    # 按段落分割，取完整段落凑满目标字数
    paragraphs = [p.strip() for p in cleaned.split('\n') if len(p.strip()) > 10]
    
    selected = []
    char_count = 0
    for para in paragraphs:
        if char_count >= target_chars:
            break
        selected.append(para)
        char_count += len(para)

    voiceover_text = '\n\n'.join(selected)

    # 确保在完整句子处截断
    if len(voiceover_text) > target_chars:
        cutoff = voiceover_text[:target_chars + 100]
        last_sentence = max(cutoff.rfind('。'), cutoff.rfind('！'), cutoff.rfind('？'))
        if last_sentence > target_chars // 2:
            voiceover_text = cutoff[:last_sentence + 1]

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# CS25 第一讲 - 配音脚本（精华版）\n\n")
        f.write(f"字数统计：约 {len(voiceover_text)} 字\n\n")
        f.write("---\n\n")
        f.write(voiceover_text)

    print(f"  配音脚本已保存: {output_path} ({len(voiceover_text)} 字)")


# ============================================================
# 主流程
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="CS25 课程转录翻译与优化")
    parser.add_argument("--input", default="output/lecture1_raw.md", help="原始转录文件")
    parser.add_argument("--output-cn", default="output/lecture1_optimized_cn.md", help="输出中文 Markdown")
    parser.add_argument("--output-script", default="output/voiceover_script.txt", help="输出配音脚本")
    parser.add_argument("--api-key", default="", help="DeepSeek API Key (也可通过 DEEPSEEK_API_KEY 环境变量设置)")
    parser.add_argument("--chunk-minutes", type=int, default=10, help="每个翻译块的分钟数")
    args = parser.parse_args()

    # API Key
    api_key = args.api_key or DEEPSEEK_API_KEY
    if not api_key:
        print("错误：请设置 DEEPSEEK_API_KEY 环境变量或通过 --api-key 参数传入")
        print("获取 API Key: https://platform.deepseek.com/api_keys")
        return 1

    os.makedirs(os.path.dirname(args.output_cn) if os.path.dirname(args.output_cn) else ".", exist_ok=True)

    # 1. 解析原始转录
    print(f"[1/4] 解析原始转录: {args.input}")
    segments = parse_raw_transcript(args.input)
    print(f"      共 {len(segments)} 个段落")

    # 2. 按时间分块
    print(f"[2/4] 按 ~{args.chunk_minutes} 分钟分块...")
    chunks = split_into_chunks(segments, args.chunk_minutes)
    print(f"      分为 {len(chunks)} 个翻译块")

    # 计算总时长
    if segments:
        total_sec = timestamp_to_seconds(segments[-1][0])
        h, m, s = total_sec // 3600, (total_sec % 3600) // 60, total_sec % 60
        total_duration = f"{int(h)}小时{int(m)}分钟{int(s)}秒"
    else:
        total_duration = "未知"

    # 3. 调用 DeepSeek API 逐块翻译
    print(f"[3/4] 调用 DeepSeek API 翻译 ({len(chunks)} 个块)...")
    client = OpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL)

    chunk_results = []
    for i, chunk in enumerate(chunks):
        chunk_text = chunk_to_text(chunk)
        result = translate_chunk(client, chunk_text, i, len(chunks))
        chunk_results.append(result)
        if i < len(chunks) - 1:
            time.sleep(1)  # 避免触发速率限制

    # 4. 组装输出 + 提取配音脚本
    print(f"[4/4] 生成输出文件...")
    full_output = assemble_full_output(chunk_results, total_duration)
    
    with open(args.output_cn, 'w', encoding='utf-8') as f:
        f.write(full_output)
    print(f"  完整中文版: {args.output_cn}")

    extract_voiceover_script(args.output_cn, args.output_script)

    print(f"\n✓ 翻译优化完成！")
    return 0


if __name__ == "__main__":
    exit(main())