---
name: wuxia-director
description: >
  Complete AI martial arts cinema direction system. Use when creating wuxia/xianxia
  fight scene prompts, storyboards, or films with AI video generation. Covers the
  full pipeline: character design, fight choreography, camera language, VFX layering,
  and quality assurance. Validated with real production data.
license: MIT
---

# AI Wuxia Director · Complete Methodology

> Consolidated from 5 days of production, 6 completed films, 5 frame-by-frame analyses,
> 4 open-source platform reverse-engineering sessions, and 2 A/B regression tests.

## Pipeline: 7 Steps From Story to Film {#pipeline}

```
① SPEC      → Duration (15s primary), aspect ratio (9:16), intensity, speed tier
② FRAMEWORK → Match scene type to battle skeleton (see references/02)
③ LEDGER    → Write combat ledger: each round must change at least one outcome
④ DRAFT     → Write prompt in Reverse-Engineering Format (see references/04)
⑤ LIGHTING  → Select and paste one lighting preset module (see templates/lighting-presets.md)
⑥ GATE      → Pass all 4 quality gates (see below)
⑦ DELIVER   → Generate → download → edit at 1.35x → publish
```

## The 12 Iron Rules {#rules}

*Every rule validated by at least one A/B test or frame-by-frame analysis. Violating any rule = rework.*

### Combat & Action

**Rule 1 — Segment or Fail**
One generation = one action process (attack / counter / collision). Never ask AI to render multi-strike choreography in a single generation. The model will compress excess actions until invisible.
```
❌ "Three rapid strikes exchanged"
✅ Segment A: strike + block
   Segment B: counter + dodge
   Segment C: final clash + impact wave
   → Edit segments at 1.35x speed
```

**Rule 2 — Two Events Maximum Per Shot**
Each timed block contains at most 2 events. Slow motion appears once per film (the decisive moment).

**Rule 3 — State Chain + Secondary Reaction**
Every shot: `start state → single action (trigger/contact/result) → end state` plus one secondary reaction (cloak fluttering, dust settling, embers fading).

### Visual Control

**Rule 4 — First-Frame Occupancy Lock**
The first visible frame must contain all required characters in correct positions. No empty establishing shots. No delayed character reveals. No abstract fillers.

**Rule 5 — Measurable Spatial Language**
Write positions as measurements, not vague words.
```
❌ "near the pillar" / "dozens of soldiers"
✅ "within 1 meter of the pillar" / "soldiers fill both flanks and depth, 3 in sharp foreground focus"
```

**Rule 6 — Physics Lock**
Enforce: weight transfer, cloth/hair delay, weapon mass (wrist angle reacts to mass, acceleration/deceleration). Prohibit: floating bodies, weightless weapons, frictionless feet, teleporting.

### Camera & Rhythm

**Rule 7 — Six-Item Camera Specification**
Every shot specifies: scene space / starting frame / character blocking / camera movement / lens & focus / endpoint & rhythm. One camera movement per shot.

**Rule 8 — Emotion as Lens Behavior**
Translate emotions into observable physical actions:
```
❌ "he looks angry"
✅ "pupils contract with reflected blade light / fist tightens, veins rise on hand / smile freezes then shatters, eyes redden"
```

### Aesthetic Standards

**Rule 9 — Eastern Beauty Anchor**
Protagonists must be young (20s), East Asian featured (flat brow ridge, shallow eye sockets, monolid/narrow phoenix eyes, black irises, soft jawline). Explicitly state "Chinese/Eastern facial features" or the model drifts to Western deep-set faces.

**Rule 10 — Material Collision**
Visual interest comes from contrasting materials (silk × metal, rough cloth × polished blade), not from color variety. One dominant color + one accent color per film.

### Generation Discipline

**Rule 11 — Sell the Hit**
Prioritize environmental impact waves (snow spray/petal burst/cracked ground). For body contact: hide the contact point (camera behind attacker's shoulder) + show the reaction (head snaps in force direction) + sound + aftermath.

**Rule 12 — Sound Timeline**
Sound starts on the first frame. Pre-strike: ambient silence. Impact: peak loudness. Post-strike: one-beat silence. Closing: half-beat fade.

## The 4 Quality Gates {#gates}

Every prompt must pass ALL gates before generation. Every film must pass before publication.

### Gate 1 — Technical QA (Objective)
- [ ] Fingers normal? Weapons unbent?
- [ ] No face morphing across shots?
- [ ] No body clipping / teleporting?
- [ ] Fallen characters remain visible?
- [ ] No AI-generated text/watermarks?

### Gate 2 — Silent Self-QA (CINEDANCE)
- [ ] All @tags actually used?
- [ ] Props in correct hands?
- [ ] Actions physically possible?
- [ ] Time blocks consistent?
- [ ] First frame correct?
- [ ] Every character's position/gaze clear?
- [ ] Lighting not flat?
- [ ] QA hidden from output?

### Gate 3 — Aesthetic Judgment (Subjective)
- [ ] Eastern face anchor present?
- [ ] Material collision (silk × metal)?
- [ ] One dominant color + one accent?
- [ ] Hair-light rim glow?
- [ ] Bokeh background (architecture/candles)?
- [ ] User has final veto

### Gate 4 — Platform Compliance
- [ ] Violence softened (weapons shatter, not people)
- [ ] No blood/gore keywords
- [ ] No copyrighted character names
- [ ] AI-generated content label checked
- [ ] Platform-safe language only

## Reverse-Engineering Format (Master Template)

```markdown
【人物固有资产】(Character Fixed Assets — repeat verbatim every segment)
Character N: <age, ethnicity, face details (Eastern anchor), eyes, hair, 
clothing materials, weapons, quality descriptors>

【固定锚点】(Fixed Anchors — repeat verbatim every segment)
<Scene, sky, ground, color system, rendering quality>

【光线布置】(Lighting Setup — paste from presets, one only)
<Light direction, quality, falloff, ambient, mood>

0-1.5s: <extreme close-up: eye/pupil reflecting threat, sound>
1.5-4s: <pull back to wide shot: spatial reveal, threat density, sound builds>
4-9s: <combat escalation: segmented actions, energy trails, impact>
9-12s: <decisive moment: THE one slow-motion, color inversion, maximum VFX>
12-15s: <hero freeze: silhouette, aftermath, particles, half-beat fade>

【交接状态】<Final frame state = next segment's starting state>
【声音时间线】<Second-by-second sound events>

Negatives: no text/watermarks, normal proportions, no extra movements
```

## Model Strategy

| Tier | Cost (15s) | Quality | Use For |
|---|---|---|---|
| Premium (Seedance 2.5) | ~300 credits (~¥13.5) | 9/10 action | Final production |
| Standard (Seedance 2.0 mini) | ~90 credits (~¥4) | 6/10 | Drafts, testing |

**Budget circuit breaker**: Max 2 re-rolls per shot. On 3rd failure, revise prompt instead. Monthly ceiling: 2000 credits.

## Asset Management

- Every character gets a three-view sheet (front/side/back) before any video generation
- Assets named: `@char_<name>_v<version>` — referenced by ID, never by filename
- Registry file tracks all assets with usage logs and deprecation status
- Style consistency: same style suffix + same character reference image across ALL shots in a film

## Fight Frameworks (Quick Reference)

| Type | Skeleton | Best For |
|---|---|---|
| One vs Many | Wide establish → staggered attacks → use-enemy-as-shield → keep fallen visible → count survivors | 1vN crowd fights |
| Duel | Trading blows → momentum shifts → weapon lock → decisive strike | 1v1 climactic battles |
| Ranged Energy | Power-up → projectile exchange → shield/deflect → ultimate beam | Magic/cultivation battles |
| Solo Breakthrough | Route establish → obstacle 1 → obstacle 2 → final barrier → escape/stop | Chases, escapes |

## The VFX Density Layer

Visual effects are not garnish — they are the main course. Every action beat needs:

| Moment | VFX Requirement |
|---|---|
| Power-up | Energy cracks on weapon, air distortion, floating debris |
| Movement | Energy trail (comet tail), speed lines, environmental disruption |
| Impact | Cross/ring shockwave, particle burst, ground fissure with glow |
| Bullet-time | Frozen particles, reflected light on suspended debris, hair suspended |
| Finish | Chain reaction (mountain collapse), lingering energy, slow-dissipating particles |

## References

- `references/01-camera-language.md` — 12 movements with prompts and verification checks
- `references/02-fight-choreography.md` — Combat ledger, frameworks, density tables
- `references/03-lighting-color.md` — 8 presets, color theory, director style cards
- `references/04-prompt-format.md` — Full reverse-engineering format specification
- `references/05-vfx-layer.md` — VFX density rules and templates
- `references/06-production-pipeline.md` — CLI automation, budget, asset registry

## Templates

- `templates/character-sheet.md` — Character design card prompt
- `templates/storyboard-format.md` — Shot-by-shot template
- `templates/scene-library.md` — 10 wuxia scenes with complete prompts
- `templates/emotion-vocabulary.md` — 80 emotions as physical behaviors
- `templates/lighting-presets.md` — 8 ready-to-paste modules
- `templates/fight-frameworks.md` — 4 battle type skeletons

## Examples

- `examples/01-sword-cold-nineteen-states.md` — Full production: "One sword chills 19 provinces"
- `examples/02-moonlit-twins.md` — Full production: identity reveal duel
- `examples/film-analysis-template.md` — Automated QA analysis report template
