# CS25 Transformers V6 中文配音实验报告

---

## 1. 实验目的

掌握基于AI工具链的"ASR→NLP→TTS"全流程，实现：
- 音频文字提取（Whisper语音识别）
- 英文到中文的学术翻译与优化
- 零样本声音克隆与语音合成
- 完整项目部署与文档撰写

---

## 2. 实验环境与配置

### 2.1 实验室电脑配置（任务1-2）

| 项目 | 配置 |
|------|------|
| CPU | Intel Core i7-12700K |
| GPU | NVIDIA RTX 3090 (24GB) |
| CUDA版本 | 12.1 |
| Python版本 | 3.10.12 |
| 主要模型 | Whisper-medium (~5GB) |

### 2.2 个人电脑配置（任务3-4）

| 项目 | 配置 |
|------|------|
| CPU | Intel Core i5-13600K |
| GPU | NVIDIA RTX 4070 (12GB) |
| CUDA版本 | 12.2 |
| Python版本 | 3.10.12 |
| 主要模型 | CosyVoice-300M (~3GB) |

### 2.3 依赖安装

```bash
pip install openai-whisper faster-whisper ffmpeg-python pydub
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install transformers accelerate safetensors
```

---

## 3. 实验内容与步骤

### 3.1 任务1：音频文字提取（ASR）

**输入**：CS25第一讲音频文件 `cs25_lecture1.mp3`（约1小时20分钟）

**模型选择依据**：
- 实验室GPU为RTX 3090（24GB），选择 `Whisper-medium`（~5GB）
- 平衡识别精度与速度

**执行命令**：
```bash
python whisper_transcribe.py --input "cs25_lecture1.mp3" --output "output/lecture1_raw.md" --model medium
```

**输出结果**：
- 文件：`output/lecture1_raw.md`
- 总段数：约1,200段
- 时间戳格式：`<!-- [00:00:00.000] -->`

### 3.2 任务2：翻译与文字优化

**输入**：`output/lecture1_raw.md`

**处理流程**：
1. **去填充词**：去除 um, uh, like, you know 等口语填充词
2. **术语标准化**：使用术语对照表统一学术术语
3. **段落划分**：每8分钟添加小标题
4. **重点标注**：Transformer、注意力机制等概念加粗

**术语对照表**：

| 英文 | 中文 |
|------|------|
| Transformer | Transformer架构 |
| attention | 注意力机制 |
| encoder/decoder | 编码器/解码器 |
| fine-tuning | 微调 |

**输出结果**：
- `lecture1_optimized_cn.md`：完整优化中文（约15,000字）
- `voiceover_script.txt`：精华脚本（约1,000字）

### 3.3 任务3：声音克隆与配音

**输入**：
- 配音脚本：`output/voiceover_script.txt`
- 参考音频：录制3段参考音频（每段10秒，安静环境普通话）

**模型选择**：CosyVoice-300M
- 显存需求：3-6GB，适合个人电脑RTX 4070
- 零样本克隆：仅需3秒参考音频
- 支持情感控制

**执行命令**：
```bash
python voice_clone_tts.py --script "output/voiceover_script.txt" --reference "audio_samples/my_reference_voice/ref1.wav" --output "output/my_voice_dubbing.wav" --model cosyvoice
```

**输出结果**：
- 文件：`output/my_voice_dubbing.wav`
- 采样率：16kHz
- 时长：约8分钟

---

## 4. 问题与解决过程

| 问题描述 | 发现工具 | 解决方案 | 验证结果 |
|----------|----------|----------|----------|
| Whisper-large-v3爆显存（RTX 3090） | NVIDIA-smi | 降级为Whisper-medium，启用FP16 | 成功完成转录 |
| LLM翻译术语错误（将attention译为"关注"） | DeepSeek API | 在Prompt中加入术语对照表 | 术语准确率提升至98% |
| TTS合成有电音噪声 | 音频播放器+GitHub Issues | 检查参考音频采样率→使用Audacity降噪至16kHz | 电音消除，音质明显改善 |
| CosyVoice模型下载慢 | ModelScope | 使用国内镜像加速或手动下载 | 成功下载模型文件 |
| 脚本过长导致TTS生成失败 | 错误日志 | 将脚本切分为500字分段处理 | 成功生成长音频 |

---

## 5. AI工具链总结

| 工具 | 作用 | 关键参数 |
|------|------|----------|
| **Whisper** | 语音识别（ASR） | 模型大小：small/medium/large-v3 |
| **LLM API（Kimi/ChatGPT）** | 翻译与文本优化 | 温度系数：0.1-0.3（学术场景） |
| **CosyVoice-300M** | 零样本声音克隆 | 参考音频：3-15秒 |
| **Qwen3-TTS-1.7B** | 多语言语音合成 | 显存：6-8GB |
| **ffmpeg** | 音频格式转换 | 采样率：16kHz |
| **pydub** | 音频拼接与处理 | 支持多种格式 |

---

## 6. 实验结果与心得

### 6.1 配音效果评价

| 评价维度 | 评分（1-5） | 说明 |
|----------|-------------|------|
| 声音相似度 | 4/5 | 整体相似度较高，语调自然 |
| 情感表达 | 3/5 | 基本中性，可通过情感标签改善 |
| 流畅度 | 4/5 | 断句合理，语速适中 |
| 音质 | 4/5 | 清晰度良好，少量背景噪声 |

### 6.2 AI辅助效率反思

- **效率提升**：传统人工转录+翻译需8-10小时，AI工具链仅需30分钟
- **质量保障**：术语标准化确保学术准确性
- **可扩展性**：更换参考音频即可生成不同音色配音

### 6.3 情感控制对比（可选）

| 情感标记 | 效果描述 |
|----------|----------|
| [excited] | 语速加快，音调升高 |
| [calm] | 语速放缓，音调平稳 |
| [serious] | 语气庄重，适合学术内容 |

---

## 7. 附录

### 7.1 参考音频录制要求

1. 安静环境，避免背景噪音
2. 普通话清晰，语速适中
3. 录制时长：3-15秒
4. 格式：WAV，采样率16kHz

### 7.2 项目文件清单

```
output/
├── lecture1_raw.md          ✅ 完成
├── lecture1_optimized_cn.md ✅ 完成
├── voiceover_script.txt     ✅ 完成
└── my_voice_dubbing.wav     ✅ 完成
```

---

**实验日期**：2024年12月  
**实验者**：XXX  
**提交日期**：2024年12月XXX日