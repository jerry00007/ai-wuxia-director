# Film Analysis (拉片) Template

> Automated QA pipeline: ffprobe → scene detection → frame extraction → VLM analysis
> Use for both competitor analysis and self-QA

## Pipeline

```bash
# 1. Technical specs
ffprobe -v error -show_entries format=duration,size,bit_rate \
  -show_entries stream=codec_type,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 video.mp4

# 2. Scene cut detection (adjust threshold 0.2-0.3)
ffmpeg -i video.mp4 -vf "select='gt(scene,0.25)',showinfo" -f null - 2>&1 \
  | grep -o 'pts_time:[0-9.]*' | sed 's/pts_time://'

# 3. Contact sheet (overview)
ffmpeg -y -v error -i video.mp4 -vf "fps=10/15,scale=400:-1,tile=5x2" \
  -frames:v 1 sheet.jpg

# 4. Key frames (specific timestamps)
for t in 1 3.5 7 10.5 13.5; do
  ffmpeg -y -v error -ss $t -i video.mp4 -frames:v 1 -q:v 3 key_$t.jpg
done
```

## VLM Analysis Prompts

### Overview (Contact Sheet)
```
这是AI生成的15秒武侠视频十格连拍(时间序)。
设计规格：[paste your shot design]。
逐格判断执行情况；再评：
1) 视觉惊艳度 1-10
2) 最出彩的一格
3) 最弱的一格
4) 有无崩坏(手指/穿模/换脸)
```

### Character Consistency Check
```
图1是角色定妆照。图2和图3是生成视频中的两帧。
对比：视频中人物与定妆照的一致度(1-10)：
脸型/疤痕/发型/服装/武器。
结论：这个角色资产能否用于后续镜头。
```

### Fight Quality Check
```
这是打斗段的连拍。按五项标准打分(1-10)：
1) 主动进攻动作明确
2) 格挡与反击真实
3) 脚步腰部重心自然变化
4) 剑刃接触点清晰有力量反馈
5) 节奏变化不像连续摆拍
```

## Report Template

```markdown
# 拉片报告 · [Title]

## 技术参数
[duration, resolution, fps, bitrate]

## 镜头清单与节奏
[shot list with timestamps, average shot length]

## 执行度
| 设计镜头 | 执行 | 偏差 |
|---------|------|------|

## 结论
- 为什么好/不好
- 3条可偷师的要点
```
