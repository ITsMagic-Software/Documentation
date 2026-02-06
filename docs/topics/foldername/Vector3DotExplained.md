{@import ../../links.md}

# Vector3.dot Explained

`Vector3.dot` (dot product) measures directional alignment between two 3D vectors.

## Formula

For vectors `a = (ax, ay, az)` and `b = (bx, by, bz)`:

```text
a · b = ax * bx + ay * by + az * bz
```

If both vectors are normalized (`|a| = 1` and `|b| = 1`):

```text
a · b = cos(theta)
```

`theta` is the angle between the vectors.

## Meaning of the result

- `dot > 0`: vectors point mostly in the same direction.
- `dot = 0`: vectors are perpendicular (`90°`).
- `dot < 0`: vectors point in opposite directions.
- `dot = 1`: exact same direction (normalized case).
- `dot = -1`: exact opposite direction (normalized case).

## Why this is useful in games

- **Field-of-view checks**: determine whether a target is in front of an NPC or camera.
- **Lighting (Lambert diffuse)**: `max(0, normal · lightDir)`.
- **Movement alignment**: detect whether input follows facing direction.
- **Surface orientation checks**: identify up-facing vs side-facing surfaces.

## Interactive animation (p5.js)

<iframe
  src="/htmls/vector3-dot-explained.html"
  title="Vector3 dot product interactive animation"
  width="100%"
  height="460"
  style="border:1px solid #2f2f2f;border-radius:8px;background:#121212;"
  loading="lazy"
></iframe>

## How to read the animation

- Vector **A** is fixed on the x-axis.
- Vector **B** rotates around the origin.
- The HUD shows:
  - `dot(A, B)`
  - `theta` in degrees.
- Color indicates sign:
  - **Blue**: positive (same-side alignment)
  - **Yellow**: near zero (almost perpendicular)
  - **Red**: negative (opposite-facing)

## Interpretation walkthrough

As `B` rotates:

1. Near `0°`, the vectors align and `dot` approaches `1`.
2. Near `90°`, they are perpendicular and `dot` approaches `0`.
3. Near `180°`, they oppose each other and `dot` approaches `-1`.

This gives an immediate visual intuition for how direction and angle affect dot product output.
