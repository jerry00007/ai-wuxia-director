# Camera Language for AI Video

## Six-Item Camera Specification

Every shot must specify ALL six items:

| Item | What to Write | Example |
|---|---|---|
| Scene Space | Subject, background, layers, relative position | "Woman sits behind desk, door behind her screen-right" |
| Starting Frame | Shot size, orientation, camera height, composition | "Eye-level medium shot, subject left third" |
| Character Blocking | Action, path, gaze, sequence | "She stops writing, looks up toward door screen-right" |
| Camera Movement | Displacement/rotation, direction, path, speed | "Camera pans slowly right from fixed position" |
| Lens & Focus | Zoom? Focus follows whom? DOF? | "Fixed focal length, face stays sharp" |
| Endpoint & Rhythm | What appears last, when to stop | "Person at door enters frame, hold one beat" |

## 12 Camera Movements (Fixed Position)

### 1. Locked-off Shot
Camera position, angle, and framing all fixed. People/light can move.
**PROMPT**: "A continuous locked-off shot. Eye-level medium shot, woman behind desk, screen-left. She stops writing, looks screen-right, puts down pen. Camera position, angle, and framing remain fixed throughout."
**Check**: Static background edges stable? Model didn't secretly add slow push?

### 2. Pan
Fixed position, rotates left/right. Follows subject or shifts attention.
**PROMPT**: "Eye-level medium shot. Camera initially faces woman behind desk. She looks screen-right, camera pans slowly right along the wall, stops on man standing in doorway, settling to medium shot."
**Check**: Did camera become a lateral slide instead? Door position consistent?

### 3. Whip Pan
Fast pan with motion blur. Same-space attention transfer or transition.
**PROMPT**: "Continuous shot. Man screen-left, woman screen-right. Camera shows man in medium shot, he suddenly looks at woman. Camera whips right with horizontal motion blur, stabilizes on woman's close-up."
**Check**: Position consistency before/after? No unwanted bounce-back?

### 4. Tilt
Fixed position, rotates up/down. Reveals along vertical axis.
**PROMPT**: "Camera at low position, wide angle, initially looking down at shoes. Tilts slowly upward past legs, torso, settles on slightly low-angle upper body."
**Check**: Pure tilt only? Camera didn't also rise?

### 5. Zoom
Fixed position, framing changes via focal length.
**PROMPT**: "Fixed camera, eye-level medium. Man seated. Lens slowly zooms in, framing tightens from waist-up to face close-up. Perspective unchanged, eyes stay sharp."
**Check**: No camera position change? No occlusion reveal?

### 6. Rack Focus
Fixed composition, focus shifts between depth layers.
**PROMPT**: "Fixed composition, shallow DOF. Foreground keys screen-left sharp, background doorway woman blurred. Focus shifts slowly to woman's eyes, keys defocus."
**Check**: Smooth transition? No object replacement?

## 6 Camera Movements (Translation)

### 7. Dolly In / Push
Camera physically moves closer. Perspective changes.
**PROMPT**: "Eye-level medium shot. Camera dollies slowly forward in straight line, fixed focal length. Framing tightens from medium to chest-up close-up. Background perspective shifts naturally."

### 8. Dolly Out / Pull Back
Camera moves away. Reveals environment.
**PROMPT**: "Start from close-up. Camera pulls back in straight line, revealing full body and surrounding empty chairs. Settles on wide shot."
**Check**: Newly revealed furniture didn't suddenly appear?

### 9. Truck (Lateral Track)
Camera moves sideways. Shows parallax and occlusion changes.
**PROMPT**: "Eye-level medium. Camera trucks slowly screen-right. Foreground pillars pass through frame, revealing what was behind them."

### 10. Pedestal (Vertical)
Camera moves up or down while maintaining angle.
**PROMPT**: "Camera starts at table edge height, looks straight ahead. Rises vertically, gaze clears table edge, revealing shelves behind."

### 11. Tracking
Camera follows moving subject. Path can be behind, side, or front.
**PROMPT**: "From behind boy's waist-up medium shot. Boy walks forward, camera follows at matching speed. Corridor doors pass frame edges. Boy stops, camera stops."

### 12. Orbit / Arc
Camera moves in arc around subject, continually facing it.
**PROMPT**: "Man stands fixed. Camera starts at his front, medium shot. Arcs to his left side, ending on his left profile. Height and distance roughly constant."
**Check**: Is camera orbiting, or is the person turning? Newly visible details consistent?

## Common Conflicts (Never Combine These)

| Conflict | Why It Fails | Fix |
|---|---|---|
| Push in + lock subject size | Camera closer = subject bigger (physics) | Subject walks backward simultaneously |
| Orbit + lock camera heading | Subject exits frame | Allow "camera continually turns to face subject" |
| Rack focus + both subjects sharp | Different depth layers need focus shift | Choose deep DOF or use performance to redirect |
| "To the right" without reference | 3 different "rights" exist | "Camera moves to subject's left side, ending on left profile" |

## Prompt Formula (Executable Instruction)

```
START: Eye-level medium shot, [subject position]
TRIGGER: [what action starts the camera move]
MOVEMENT: Camera [movement type] [direction] [speed]
END: Settles on [endpoint framing], [headroom note]
FOCUS: [what stays sharp]
CONTINUITY: [prop/environment consistency note]
```

## Text-to-Video vs Image-to-Video Writing

- **T2V**: Must describe scene, subject, starting composition, THEN camera movement
- **I2V**: First frame exists → only describe action, camera path, end state. Never contradict the reference image's clothing/position/lighting
