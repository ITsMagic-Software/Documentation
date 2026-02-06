{@import ../../links.md}

# Vector3.dot Explained

`Vector3.dot` (dot product) measures how aligned two vectors are.

```text
a · b = ax * bx + ay * by + az * bz
```

When vectors are normalized, the result is the cosine of the angle between them:

```text
a · b = cos(theta)
```

- `dot > 0`: similar direction.
- `dot = 0`: perpendicular.
- `dot < 0`: opposite direction.

## Interactive animation (p5.js)

<iframe
  src="/htmls/vector3-dot-explained.html"
  title="Vector3 dot product interactive animation"
  width="100%"
  height="460"
  style={{ border: '1px solid #2f2f2f', borderRadius: '8px', background: '#121212' }}
  loading="lazy"
/>

## How to read the animation

- Vector **A** is fixed.
- Vector **B** rotates continuously.
- The HUD shows the live values for `dot(A, B)` and `theta`.
- Colors indicate sign:
  - Blue: positive dot.
  - Yellow: near zero.
  - Red: negative dot.

## Common use cases in games

- Vision cone / field-of-view checks.
- Lighting calculations with surface normals.
- AI facing checks and target validation.
- Movement alignment and directional filtering.
