# The Reverse-Engineering Format

> Discovered by feeding a viral video into 即梦/Dreamina's built-in "video analysis" feature. The output format is the model's native language — prompts written this way achieve 90%+ specification compliance vs ~40% for hand-written prose.

## Complete Template

```markdown
【人物固有资产】
Character 1: <detailed physical description with Eastern face anchor, hair, clothing materials, weapon, quality descriptors>
Character 2: <same level of detail if applicable>
(Repeat this block VERBATIM in every segment — one character change = full reshoot)

【固定锚点】
<Scene, sky condition, ground surface, overall color scheme, rendering quality tier>
(Repeat VERBATIM in every segment)

【光线布置】
<One lighting preset from the library, adapted to this scene>

0-1.5s: <HOOK: extreme close-up (eye/pupil/weapon detail), first frame sound>
1.5-4s: <ESTABLISH: pull back to wide, spatial reveal, threat density>
4-9s: <ESCALATION: combat/action, segmented by second, energy trails, environmental destruction>
9-12s: <DECISIVE: THE one slow-motion, color reversal, maximum VFX density>
12-15s: <RESOLVE: hero freeze, aftermath, particles settling, half-beat audio fade>

【交接状态】<Exact description of final frame = starting state of next segment>

【声音时间线】
<Second-by-second: ambient → buildup → peak → silence beat → aftermath>

Negatives: no text/watermarks, normal proportions, no extra movements, weapons unbent, fingers normal
```

## Key Rules

1. **固有资产 repeats verbatim** — never paraphrase between segments
2. **Time blocks are 1-3 seconds each** — finer than narrative beats
3. **硬切 (hard cut) must be explicitly written** — model won't cut on its own
4. **交接状态 chains segments** — end state = next start state
5. **Sound timeline is separate from visual** — model generates audio simultaneously
6. **Negative constraints at the end** — standard list, always include

## Adaptation for Different Durations

| Duration | Blocks | Notes |
|---|---|---|
| 5s | 2 blocks | Hook + single action |
| 10s | 4 blocks | Mini-arc: setup → action → peak → settle |
| 15s | 5-6 blocks | Standard short: full arc |
| 30s | 2×15s segments | Chain via 交接状态 |

## Adaptation for T2V vs I2V

- **Text-to-Video**: Full format including visual anchors
- **Image-to-Video**: Keep 固有资产 + 固定锚点 + sound. Replace visual description with: "图1 is the keyframe for this shot" + only describe ACTION, camera path, and end state
