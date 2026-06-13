# Stanford CS25 Transformers V6 - AI中文配音项目

基于AI工具链的LLM课程中文配音项目，实现"ASR → 翻译 → 声音克隆 → 配音"全流程自动化。

## 功能特性

- **ASR语音识别**：基于 OpenAI Whisper，支持多尺寸模型
- **学术翻译优化**：通过LLM API将英文转录翻译为学术化中文，自动处理术语标准化
- **零样本声音克隆**：使用 MOSS-TTS-Nano 轻量模型，纯 CPU 运行，无需 GPU
- **多TTS后端支持**：内置 Edge-TTS（在线）、CosyVoice（GPU）、MOSS-TTS-Nano（CPU）三种方案

---

## 项目结构

```
.
├── README.md                           # 项目说明文档（本文档）
├── requirements.txt                    # Python 依赖清单
├── .gitignore                          # Git 忽略规则
├── experiment_report.md                # 实验报告
│
├── Task1/                              # 任务一：音频文字提取（ASR）
│   ├── whisper_transcribe.py           # Whisper 转录脚本
│   └── lecture1_raw.md                 # 原始英文转录结果
│
├── Task2/                              # 任务二：翻译与优化
│   ├── translate_optimize.py           # LLM 翻译优化脚本
│   └── lecture1_optimized_cn.md        # 优化后中文讲稿
│
└── Task3/                              # 任务三：声音克隆与配音
    ├── generate_dubbing.py             # 配音生成主脚本（支持多种TTS后端）
    ├── voice_clone_tts.py              # 声音克隆脚本（CosyVoice / Qwen3-TTS）
    ├── ref_01.wav                      # 参考音色音频（待克隆的目标声音）
    ├── sample_500.txt                  # 500字中文配音文本（示例）
    ├── voiceover_script.txt            # 完整配音脚本
    ├── MOSS-TTS-Nano-main/             # MOSS-TTS-Nano 轻量TTS模型源码
    │   ├── infer_onnx.py               # ONNX 推理入口
    │   ├── onnx_tts_runtime.py         # ONNX 运行时封装
    │   └── ...
    └── output/                         # 输出目录
        ├── clone_500.wav               # 最终克隆音色配音示例（约2分22秒）
        ├── dubbing.mp3                 # Edge-TTS 备用配音
        └── ref_01_10s_24k_mono.wav     # 预处理后参考音频
```

---

## 环境要求

| 组件 | 最低配置 | 推荐配置 |
|------|----------|----------|
| CPU | 任意 x86_64 | Intel i5 / AMD Ryzen 5 及以上 |
| 内存 | 4 GB | 8 GB 及以上 |
| GPU | 无需 GPU | 可选（CosyVoice 方案需 6GB+ 显存） |
| 磁盘空间 | 2 GB | 5 GB（含模型缓存） |
| 操作系统 | Windows 10 / Ubuntu 20.04 / macOS 12 | Windows 11 / Ubuntu 22.04 |

> **提示**：本项目主打方案（MOSS-TTS-Nano ONNX）完全基于 CPU 推理，无 NVIDIA 显卡亦可运行。

---

## 依赖安装

### 1. 安装系统依赖

- **ffmpeg**（音频格式转换必需）
  - Windows：从 [ffmpeg 官网](https://ffmpeg.org/download.html) 下载，将 `bin` 目录加入系统 PATH
  - Ubuntu：`sudo apt update && sudo apt install ffmpeg`
  - macOS：`brew install ffmpeg`

### 2. 安装 Python 依赖

```bash
# 进入项目根目录
cd stanford-cs25-dubbing-ai

# 安装全部 Python 依赖
pip install -r requirements.txt
```

`requirements.txt` 核心依赖说明：

| 依赖包 | 用途 |
|--------|------|
| `openai-whisper` | 语音识别（ASR） |
| `transformers` | HuggingFace 模型加载 |
| `torch`, `torchaudio` | PyTorch 深度学习框架及音频处理 |
| `onnxruntime` | ONNX 模型推理（MOSS-TTS-Nano 必需） |
| `modelscope` | 国内模型下载通道 |
| `edge-tts` | 微软在线 TTS 备用方案 |
| `tqdm` | 进度条显示 |

### 3. 安装 MOSS-TTS-Nano（已内置源码）

本项目已将 `MOSS-TTS-Nano` 源码置于 `Task3/MOSS-TTS-Nano-main/` 目录下。**首次运行时会自动从 HuggingFace / ModelScope 下载 ONNX 模型文件（约 700MB）到本地缓存**。

如需手动预下载模型，可执行：

```bash
pip install modelscope
python -c "from modelscope import snapshot_download; snapshot_download('openmoss/MOSS-TTS-Nano'); snapshot_download('openmoss/MOSS-Audio-Tokenizer-Nano')"
```

> 模型默认缓存路径：`C:\Users\<用户名>\.cache\modelscope\hub\`（Windows）或 `~/.cache/modelscope/hub/`（Linux/macOS）。

---

## 快速开始

### 步骤一：音频转文字

```bash
cd Task1
python whisper_transcribe.py \
  --input "llm01.m4a" \
  --output "lecture1_raw.md" \
  --model medium
```

参数说明：
- `--input`：输入音频文件路径（支持 mp3、m4a、wav 等格式）
- `--output`：输出 Markdown 文件路径
- `--model`：Whisper 模型尺寸，可选 `tiny` / `base` / `small` / `medium` / `large-v3`

### 步骤二：翻译与优化

```bash
cd Task2
python translate_optimize.py \
  --input "lecture1_raw.md" \
  --output-cn "lecture1_optimized_cn.md" \
  --output-script "voiceover_script.txt"
```

脚本会自动去除口语填充词、标准化学术术语，并将长文本切分为适合配音的段落。

### 步骤三：声音克隆配音

#### 方案 A：MOSS-TTS-Nano（推荐，纯 CPU）

直接调用 ONNX 推理脚本，获取最佳克隆效果：

```bash
cd Task3

# 基础使用（自动下载模型）
python MOSS-TTS-Nano-main/infer_onnx.py \
  --mode voice_clone \
  --prompt-audio-path "ref_01.wav" \
  --text "大家好，欢迎来到斯坦福大学课程。我是主讲人..." \
  --output-audio-path "output/my_clone.wav" \
  --device cpu
```

关键参数说明：

| 参数 | 说明 |
|------|------|
| `--mode` | 推理模式：`voice_clone`（音色克隆）或 `continuation`（音频续写） |
| `--prompt-audio-path` | 参考音频路径（建议 3–10 秒，WAV 格式） |
| `--text` | 待合成的中文文本 |
| `--output-audio-path` | 输出音频路径 |
| `--device` | 计算设备：`cpu` 或 `cuda` |
| `--disable-wetext-processing` | 禁用 WeTextProcessing（Windows 环境建议加上） |

#### 方案 B：Edge-TTS（极速在线，无音色克隆）

仅需网络连接，1 分钟内完成：

```bash
cd Task3
python generate_dubbing.py \
  --script "sample_500.txt" \
  --output "output/dubbing.mp3" \
  --model edge-tts
```

#### 方案 C：CosyVoice（高质量，需 GPU）

```bash
cd Task3
python generate_dubbing.py \
  --script "sample_500.txt" \
  --reference "ref_01.wav" \
  --output "output/cosyvoice_dubbing.wav" \
  --model cosyvoice
```

> 使用 CosyVoice 前需先安装：[CosyVoice 官方仓库](https://github.com/FunAudioLLM/CosyVoice)

---

## 克隆音色使用详解

### 1. 准备参考音频

参考音频的质量直接决定克隆效果。建议按以下标准录制：

- **环境**：安静、无回声、无背景噪音
- **内容**：清晰的普通话，避免方言或口音
- **时长**：3–10 秒（MOSS-TTS-Nano 对短音频友好）
- **格式**：WAV，单声道，采样率 ≥ 16kHz
- **音量**：正常说话音量，避免过大或过小

如已有音频不符合标准，可用 ffmpeg 预处理：

```bash
# 截取前10秒，转为单声道24kHz WAV（MOSS-TTS-Nano推荐格式）
ffmpeg -i ref_01.wav -ar 24000 -ac 1 -t 10 -y ref_01_10s_24k_mono.wav
```

### 2. 长文本分段处理

当待合成文本超过 200 字时，建议按语义切分为多段，分别生成后再拼接，以避免显存/内存溢出或音质下降。

本项目 `Task3/output/clone_500.wav` 即采用分段生成策略：将约 700 字文本按自然断句切分为 7 段，每段约 100 字，依次调用 ONNX 推理后合并。

### 3. 自定义脚本生成

若需为自有文本生成配音，只需：

1. 将文本保存为 `.txt` 文件（UTF-8 编码）
2. 替换 `--text` 参数中的内容，或修改 `sample_500.txt`
3. 运行上述推理命令

---

## 常见问题

**Q1：Whisper 转录时显存不足？**

将模型降级为 `small` 或 `base`，并开启半精度：
```bash
python whisper_transcribe.py --input "audio.m4a" --model small --fp16
```

**Q2：MOSS-TTS-Nano 首次运行下载模型很慢？**

配置国内镜像加速：
```bash
set HF_ENDPOINT=https://hf-mirror.com        # Windows CMD
$env:HF_ENDPOINT="https://hf-mirror.com"    # Windows PowerShell
export HF_ENDPOINT=https://hf-mirror.com     # Linux/macOS
```

**Q3：Windows 下运行 ONNX 推理报 DLL 错误？**

确保 `onnxruntime` 与 `torchaudio` 版本兼容。推荐组合：
```
onnxruntime==1.16.3
torchaudio==2.0.2
torch==2.0.1
```

**Q4：克隆出的音色不像？**

- 检查参考音频是否有背景噪音，建议使用 Audacity 降噪
- 确保参考音频与目标文本语言一致（均为中文）
- 尝试使用更短的参考音频（3–5 秒）重新生成

**Q5：生成音频有电音/杂音？**

- 将参考音频统一转为 24kHz 单声道 WAV
- 避免参考音频末尾有截断或爆音

---

## 致谢

- [OpenAI Whisper](https://github.com/openai/whisper) - 开源语音识别模型
- [MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) (OpenMOSS) - 轻量级零样本声音克隆
- [Edge-TTS](https://github.com/rany2/edge-tts) - 微软 Edge 在线文本转语音
- [Stanford CS25](https://web.stanford.edu/class/cs25/) - Transformers V6 课程

---

## 许可证

MIT License
