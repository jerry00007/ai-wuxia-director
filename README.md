# AI Wuxia Director

> **QA Engineer's approach to AI martial arts cinema.**
> A complete methodology for producing cinematic wuxia/xianxia short films with AI video generation — from a unique perspective that combines film language, combat choreography, quality assurance, and production automation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Chinese](https://img.shields.io/badge/中文-README.md-red)](README.md)

## Why This Exists

AI video tools (Seedance, Kling, Vidu, etc.) have made "generating a clip" trivially easy. But producing a **15-30 second short film that looks like cinema** — with consistent characters, real fight choreography, proper camera language, and emotional rhythm — is still hard.

Most tutorials teach you how to write a prompt. This project teaches you how to **think like a director, choreograph like a fight coordinator, and QA like a test engineer**.

## What Makes This Different

| Existing Approach | This Project |
|---|---|
| "Write a beautiful prompt" | **7-step production pipeline with quality gates** |
| One-shot generation | **Segment-based choreography** (one action per generation) |
| Hope for the best | **12 iron rules validated by A/B testing and frame-by-frame analysis** |
| Manual trial-and-error | **Automated CLI pipeline + budget circuit breakers** |
| Generic "cinematic" style | **Wuxia/xianxia specialized: combat frameworks, energy aesthetics, Eastern facial anchors** |

## Quick Start

### For AI Agents (Claude Code, OpenClaw, Codex, etc.)

Install as a skill:

```bash
npx skills add your-username/ai-wuxia-director
```

Then just say: *"Use wuxia-director to create a 15-second fight scene"*

### For Humans

Read [SKILL.md](SKILL.md) for the complete methodology. Start with:
1. [The 7-Step Pipeline](SKILL.md#pipeline) — from story to finished film
2. [The 12 Iron Rules](SKILL.md#rules) — validated prompt engineering laws
3. [The 4 Quality Gates](SKILL.md#gates) — never ship without QA

## Repository Structure

```
ai-wuxia-director/
├── SKILL.md                        # Master methodology (start here)
├── references/
│   ├── 01-camera-language.md       # 12 camera movements + PROMPT templates + verification checks
│   ├── 02-fight-choreography.md    # Combat ledger, 4 battle frameworks, density tables
│   ├── 03-lighting-color.md        # 8 lighting presets (copy-paste), color discipline, director styles
│   ├── 04-prompt-format.md         # The Reverse-Engineering format (Seedance native language)
│   ├── 05-vfx-layer.md             # Visual effects density: energy trails, impact frames, particles
│   └── 06-production-pipeline.md   # CLI automation, budget management, asset registry
├── templates/
│   ├── character-sheet.md          # Character design card prompt template
│   ├── storyboard-format.md        # Shot-by-shot storyboard template
│   ├── scene-library.md            # 10 wuxia scenes with full prompts
│   ├── emotion-vocabulary.md       # 80 emotions as facial muscle behavior
│   ├── lighting-presets.md         # 8 ready-to-paste lighting modules
│   └── fight-frameworks.md         # 4 battle type skeletons (1vN, duel, ranged, solo)
├── examples/
│   ├── 01-sword-cold-nineteen-states.md   # Full case: "One sword chills 19 provinces"
│   ├── 02-moonlit-twins.md                # Full case: identity reveal duel
│   └── film-analysis-template.md          # Automated QA analysis template
├── scripts/
│   ├── film_qa.py                  # Automated frame extraction + VLM analysis
│   └── batch_generate.sh           # CLI batch generation with budget circuit breaker
└── LICENSE
```

## The Core Discovery

After analyzing viral AI fight videos (3.9M+ plays), producing 6 short films, and running A/B tests, the biggest insight was:

> **AI video models don't delete excess actions — they compress them until invisible.**
>
> The fix isn't better prompts. It's **breaking one complex fight into simple, single-action segments** and assembling them in post-production.

This led to the "segment-based choreography" approach that consistently scores 9+/10:

```
❌ Traditional: "Two fighters exchange three rapid strikes" → Model renders floating poses
✅ Ours: 3 segments × 1 action each → Model renders each with real physics → Edit at 1.35x speed
```

## Validated With Real Data

| Experiment | Metric | Result |
|---|---|---|
| A/B: multi-action vs segmented prompts | VLM quality score | 6/10 vs 9/10 |
| A/B: mini vs premium model tier | Combat action quality | 6/10 vs 9/10 |
| Reverse-engineering format vs hand-written | Specification compliance | 40% vs 90% |
| Character consistency (three-view sheet method) | Cross-shot face stability | 9/10 |
| 6 films, zero re-rolls needed | Production efficiency | ~15 min per 15s film |

## Compatible Tools

| Tool | Status | Notes |
|---|---|---|
| 即梦/Dreamina (Seedance) | ✅ Primary | CLI automation available |
| 可灵/Kling | ✅ | Web UI, good action quality |
| 豆包/Doubao | ✅ | Free tier for testing |
| LibTV | ✅ | Aggregated platform |
| Vidu / Runway / others | ✅ | Format is platform-agnostic |

## Contributing

Contributions welcome! Especially:
- New scene templates (different eras/settings)
- Fight framework variations (weapon types, group dynamics)
- Language translations
- Production pipeline improvements

## License

MIT — use it commercially, fork it, build on it.

---

*Built from 5 days of production experience, 12 knowledge base articles, 5 frame-by-frame film analyses, 4 open-source platform reverse-engineering sessions, and 32 reference image transcriptions.*
