# 🎯 Stanford CS25 Transformers V6 - AI中文配音项目

基于AI工具链的LLM课程中文配音项目，实现"ASR→翻译→声音克隆→配音"全流程。

## 📋 项目概述

本项目以斯坦福大学CS25（Transformers V6）第一讲音频为素材，构建完整的AI配音流水线：

1. **ASR语音识别**：使用Whisper模型提取音频文字
2. **翻译优化**：通过LLM API将英文转录翻译为学术化中文
3. **声音克隆**：使用MOSS-TTS-Nano进行零样本声音克隆（纯CPU轻量模型）
4. **音频合成**：生成个人声音的中文配音

## 🛠️ 环境配置

### 硬件要求

| 模型 | 显存需求 | 推荐用途 |
|------|----------|----------|
| Whisper-small | ~2GB | 低显存环境转录 |
| Whisper-medium | ~5GB | 推荐转录 |
| Whisper-large-v3 | ~10GB | 高精度转录 |
| **MOSS-TTS-Nano** | **无需GPU** | **轻量声音克隆（本项目使用）** |

### 软件依赖

```bash
# 安装基础依赖
pip install -r requirements.txt

# 安装ffmpeg（系统依赖）
# Windows: https://ffmpeg.org/download.html
# Ubuntu: sudo apt install ffmpeg
# macOS: brew install ffmpeg
```

### MOSS-TTS-Nano 模型准备

本项目已内置MOSS-TTS-Nano源码（见`Task3/MOSS-TTS-Nano-main/`）。首次运行时会自动下载ONNX模型文件到本地缓存目录，也可手动下载：

```bash
# 从ModelScope下载
pip install modelscope
python -c "from modelscope import snapshot_download; snapshot_download('openmoss/MOSS-TTS-Nano'); snapshot_download('openmoss/MOSS-Audio-Tokenizer-Nano')"
```

> **注意**：ONNX模型文件约700MB，已配置在`.gitignore`中，提交GitHub时不会包含。

## 🚀 三步执行

### 步骤1：音频文字提取

```bash
cd Task1
python whisper_transcribe.py \
  --input "llm01.m4a" \
  --output "lecture1_raw.md" \
  --model medium
```

### 步骤2：翻译与优化

```bash
cd Task2
python translate_optimize.py \
  --input "lecture1_raw.md" \
  --output-cn "lecture1_optimized_cn.md" \
  --output-script "voiceover_script.txt"
```

### 步骤3：声音克隆配音

使用MOSS-TTS-Nano ONNX后端（纯CPU运行，无需GPU）：

```bash
cd Task3
python generate_dubbing.py \
  --script "sample_500.txt" \
  --reference "ref_01.wav" \
  --output "output/clone_500.wav" \
  --model moss-nano
```

> 项目已包含一段基于`ref_01.wav`参考音频生成的示例音频：`Task3/output/clone_500.wav`。

## 📁 项目结构

```
stanford-cs25-dubbing-ai/
├── README.md                    # 项目说明文档
├── requirements.txt             # 依赖清单
├── .gitignore                   # Git忽略规则
├── experiment_report.md         # 实验报告
├── Task1/                       # ASR语音识别
│   ├── whisper_transcribe.py    # Whisper转录脚本
│   └── lecture1_raw.md          # 原始英文转录结果
├── Task2/                       # 翻译与优化
│   ├── translate_optimize.py    # LLM翻译优化脚本
│   └── lecture1_optimized_cn.md # 优化后中文讲稿
└── Task3/                       # 声音克隆与配音
    ├── generate_dubbing.py      # 配音生成主脚本（支持多种TTS后端）
    ├── voice_clone_tts.py       # 声音克隆脚本（CosyVoice备用方案）
    ├── ref_01.wav               # 参考音色音频（待克隆的目标声音）
    ├── sample_500.txt           # 500字中文配音文本
    ├── voiceover_script.txt     # 完整配音脚本
    ├── MOSS-TTS-Nano-main/      # MOSS-TTS-Nano轻量TTS模型（子目录）
    │   ├── infer_onnx.py        # ONNX推理入口
    │   ├── onnx_tts_runtime.py  # ONNX运行时
    │   └── ...                  # 模型源码与配置
    └── output/                  # 输出目录
        ├── clone_500.wav        # 最终克隆音色配音（约2分22秒）
        ├── dubbing.mp3          # Edge-TTS备用配音
        └── ref_01_10s_24k_mono.wav  # 预处理后的参考音频
```

## 📝 术语对照表

| 英文术语 | 中文翻译 |
|----------|----------|
| Transformer | Transformer架构 |
| attention | 注意力机制 |
| self-attention | 自注意力机制 |
| encoder | 编码器 |
| decoder | 解码器 |
| embedding | 嵌入 |
| fine-tuning | 微调 |
| inference | 推理 |
| context window | 上下文窗口 |
| voice clone | 声音克隆 |
| TTS | 文本转语音 |

## ❓ 常见问题FAQ

**Q1: Whisper爆显存怎么办？**
- A: 降低模型级别：`--model medium` 或 `--model small`
- 添加 `--fp16` 参数启用半精度推理

**Q2: MOSS-TTS-Nano推理时程序崩溃？**
- A: 确保`sentencepiece`版本兼容（推荐`0.1.99`）
- 检查`torchaudio`与`onnxruntime`的DLL冲突（Windows环境常见问题）
- 参考音频建议裁剪为10秒以内、24kHz单声道wav格式

**Q3: 模型下载慢？**
- A: 配置国内镜像：`export HF_ENDPOINT=https://hf-mirror.com`
- 或使用ModelScope国内源下载

**Q4: 生成的音频有杂音或音质不佳？**
- A: 使用更高质量的参考音频（安静环境、清晰人声、16kHz+采样率）
- 确保参考音频无背景噪音

## 🤝 致谢

- **OpenAI Whisper** - 高精度语音识别
- **MOSS-TTS-Nano** (OpenMOSS) - 轻量级CPU友好声音克隆
- **Edge-TTS** - 在线TTS备用方案
- **Stanford CS25** - 优质课程内容

## 📄 许可证

MIT License
