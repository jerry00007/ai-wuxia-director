# Fight Choreography for AI Video

## The Combat Ledger

Before writing any fight prompt, create a ledger. Each round = 3 cells:

| Cell | Content |
|---|---|
| Initiation | Who, which hand/foot, with what weapon, from which side |
| Response | Dodge / block / catch / counter / hit taken |
| Result | Distance, facing, weapon control, injury, next-round advantage |

**Iron rule**: Each round must change at least one result. Two consecutive rounds with no change = repetition = delete.

## Segment Discipline (The #1 Discovery)

> **AI video models don't delete excess actions — they compress them until invisible.**

This means:
- ❌ "Three rapid strikes" in one generation → Model renders floating poses
- ✅ 3 segments × 1 action each → Each rendered with real physics → Edit together

| Segment | Duration | Action |
|---|---|---|
| A | 4s gen → cut to 2.5s | Strike + block |
| B | 4s gen → cut to 2.5s | Counter + dodge |
| C | 4s gen → cut to 2.5s | Final clash + impact wave |

Edit all at 1.35x speed → ~5.5 seconds of dense, realistic combat.

## 4 Battle Frameworks

### 1. One vs Many (Crowd Fight)
1. Wide shot: establish protagonist and all opponent positions
2. Staggered attacks (different directions, different rhythms)
3. Use one opponent's movement to block another
4. Keep fallen opponents visible (AI tends to erase them)
5. Ending: clear count of remaining enemies and protagonist's direction

**Rules**: Only ONE opponent attacks per round. Others wait in visible positions. When protagonist turns to face new opponent = new axis = re-establish with wide shot first.

### 2. Duel (1v1 Climactic)
Core: momentum shifts and distance struggle.
1. Establish stakes and skill parity
2. First exchange (testing)
3. Escalation (weapons lock, close quarters)
4. Decisive strike (the ONE slow motion)

### 3. Ranged Energy Battle
1. Power-up sequence (weapon glows, air distorts)
2. Projectile exchange (beams, sword qi, energy waves)
3. Shield/deflect moment
4. Ultimate technique (maximum VFX)

### 4. Solo Breakthrough (Chase/Escape)
1. Establish route and exit
2. First obstacle forces change of path
3. Second obstacle blocks original route
4. Final barrier tests established skills
5. Escape or forced stop at clear position

## Intensity & Density Tables (15s baseline)

| Parameter | High Intensity | Medium | Slow Burn |
|---|---|---|---|
| Exchanges | 7-9 | 6-8 | 5-7 |
| Micro-actions | 16-22 | 12-16 | 10-14 |
| Shots | 6-9 | 5-7 | 3-4 (or one long take) |
| First action within | 0.15s | 0.3s | acceptable to build |
| Action close-ups | 0.4-0.8s | 0.8-1.5s | — |
| Slow motion | Max 1, 0.15-0.3s | As needed | As needed |

## Selling the Hit (4 Techniques)

1. **Environmental Impact** (easiest to generate, most convincing): snow spray, ground fissure, rock shatter, water burst. Better than body contact.
2. **Hide the Contact Point**: Camera behind attacker's shoulder, punch path toward/away from lens, foreground arm blocks contact.
3. **Reaction Close-up**: Only receiver in frame, fist enters from off-screen, face snaps in force direction (direction must match!).
4. **Sound + Aftermath**: Thud + splash + stumbled retreat + bent object.

## 6 Common Failure Modes

| Failure | Fix |
|---|---|
| Action chaos / teleporting | Combat ledger + segment discipline (one action per gen) |
| Body clipping | One hold per shot in grappling; struggle via sound only |
| Face morphing | Three-view character sheet + reference image binding |
| Weapon duplication/change | Prompt specifies which hand, when dropped/picked up |
| Weak impact feeling | 4 selling techniques + impact frames |
| Camera shake | One movement per shot; vertical actions need headroom in portrait |
