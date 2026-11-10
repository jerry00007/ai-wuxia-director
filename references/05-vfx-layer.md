# VFX Density Layer

> VFX are not garnish — they are the main course. Every action beat needs visual effects. This is the difference between "clean but boring" and "viral."

## The VFX Checklist (Every Beat Must Have Something)

| Moment | Required VFX | Prompt Keywords |
|---|---|---|
| Power-up | Weapon glow, air distortion, floating debris | "剑身裂纹发亮如岩浆" "空气扭曲产生热浪涟漪" "碎石悬浮" |
| Movement | Energy trail, speed lines, environmental disruption | "残影划出白与暗红能量轨迹如彗星尾迹" |
| Impact | Shockwave, particle burst, ground fissure | "十字形银白色剑气冲击波" "同心圆向四周扩散" "冰原裂开" |
| Bullet-time | Frozen particles, light on suspended debris | "数万块冰晶碎片悬浮每块映出倒影" |
| Aftermath | Chain reaction, lingering energy | "雪山一座接一座崩塌" "暗红能量从裂纹渗出" |

## Impact Frames (from cinematic-fight-prompt)

```
原始动作定格 → 生成3-6张撞色候选图(红蓝/白黑/红黑/蓝白)
→ 选冲击关系最清楚的一张 → 作为关键参考插回视频生成
→ 检查受力结果和身份连续性
```

## Color Inversion at Climax

The most effective VFX technique discovered:
```
Before: 冷灰蓝主色调 (cold gray-blue dominant)
THE STRIKE: 锈橙爆发 (rust-orange explosion, 1-2 seconds)
After: 回归冷灰蓝 (return to cold gray-blue)
```
This is a 3-line addition to any prompt but creates the most memorable moment.

## The "Sword Cold Nineteen Provinces" Scale Technique

To convey massive scale (the "三万里" problem):
- ❌ Don't just make a bigger explosion
- ✅ Show the ENVIRONMENT reacting at distance: mountains collapsing one by one, cracks extending to the horizon, energy waves visible from space

```
"远处连绵雪山一座接一座在无声中崩塌滑落，
每座山峰断裂处迸发蓝白色能量冲击波向天空扩散"
```
