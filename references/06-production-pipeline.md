# Production Pipeline & Automation

## CLI Quick Start (Dreamina/即梦)

```bash
# Install
curl -s https://jimeng.jianying.com/cli | bash

# Login (one-time)
dreamina login

# Check balance
dreamina user_credit

# Text-to-Video (premium)
dreamina text2video \
  --prompt='<full reverse-engineering format prompt>' \
  --model_version=seedance2.5 \
  --duration=15 --ratio=9:16 --video_resolution=720p \
  --poll=600

# Image-to-Video (with reference)
dreamina multimodal2video \
  --image="character_sheet.png" \
  --image="scene_keyframe.png" \
  --prompt='<prompt with @image references>' \
  --model_version=seedance2.5 \
  --duration=15 --ratio=9:16 --video_resolution=720p \
  --poll=600

# Download
dreamina query_result --submit_id=<id> --download_dir=output/
```

## Budget Management

| Rule | Value |
|---|---|
| Max re-rolls per shot | 2 (on 3rd failure, revise prompt) |
| Monthly credit ceiling | 2000 |
| Premium (2.5) per 15s | ~300 credits (~¥13.5) |
| Draft (mini) per 15s | ~90 credits (~¥4) |
| Standard workflow | Draft with mini → verify → rerun with 2.5 |

## Asset Registry Template

```markdown
# Asset Registry

## ACTIVE
| ID | Character | Version | Path | First Used |
|----|-----------|---------|------|-----------|
| char_hero_v1 | Hero name | v1 | assets/hero.png | Episode 01 |

## DEPRECATED
| ID | Reason |
|----|--------|
| char_old_v1 | Superseded by v2 |
```

Naming convention: `@char_<name>_v<version>` — reference by ID in all prompts.

## QA Log Template

```markdown
| # | Date | Title | Pipeline | Cost | Re-rolls | Score | Notes |
|---|------|-------|----------|------|----------|-------|-------|
| 1 | | | | | | | |

## Publication Data
| Film | Published | Views | Completion | 3s Bounce | Likes | Comments | Action |
|------|-----------|-------|------------|-----------|-------|----------|--------|
```

## Editing Standards

- Speed: 1.35x on combat segments (validated by user testing)
- Audio: layer original track (0.8x) + voiceover (1.8x) + synthesized SFX hits + heartbeat accents
- Subtitles: post-production only, never AI-generated in-frame
- Color grade: add film grain filter to reduce "CG perfection" feel
