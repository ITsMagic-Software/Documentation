{@import ../../links.md}

# Vector3.dot Explained with a p5.js Animation

`Vector3.dot` (dot product) is one of the most useful operations in 3D math for games and interactive graphics. It helps you measure **how much one vector points in the same direction as another**.

## What `Vector3.dot` does

Given two vectors `a` and `b`:

```text
a · b = ax * bx + ay * by + az * bz
```

If both vectors are normalized (length `1`), then:

```text
a · b = cos(theta)
```

Where `theta` is the angle between them.

## How to read the result

- `dot > 0`: vectors point in a similar direction.
- `dot = 0`: vectors are perpendicular (90°).
- `dot < 0`: vectors point in opposite directions.
- `dot = 1`: exactly the same direction (if normalized).
- `dot = -1`: exactly opposite direction (if normalized).

## Practical use cases

- **Field of view checks** (is target in front of character/camera?).
- **Lighting** (Lambert diffuse: normal · lightDirection).
- **Input alignment** (is movement aligned with facing direction?).
- **Surface tests** (is a surface facing up, down, or sideways?).

## p5.js animation idea

The animation below rotates one vector around the origin while another remains fixed. It displays:

1. The two vectors.
2. The angle between them.
3. The dot product value updated every frame.
4. A color cue for positive/zero/negative values.

```html
<script src="https://cdn.jsdelivr.net/npm/p5@1.9.3/lib/p5.min.js"></script>
<script>
let angle = 0;

function setup() {
  createCanvas(700, 420);
  textFont('monospace');
}

function drawArrow(v, col, label) {
  push();
  stroke(col);
  fill(col);
  strokeWeight(3);
  line(0, 0, v.x, v.y);

  // Arrow head
  push();
  translate(v.x, v.y);
  rotate(v.heading());
  triangle(0, 0, -12, 6, -12, -6);
  pop();

  noStroke();
  text(label, v.x + 8, v.y + 8);
  pop();
}

function draw() {
  background(18);
  translate(width * 0.5, height * 0.55);

  // Fixed vector A (normalized)
  const a = createVector(1, 0);

  // Rotating vector B (normalized)
  const b = createVector(cos(angle), sin(angle));

  // Dot product and angle
  const dot = a.dot(b);           // in [-1, 1]
  const theta = acos(constrain(dot, -1, 1));

  // Scale vectors for visualization
  const scale = 140;
  const av = p5.Vector.mult(a, scale);
  const bv = p5.Vector.mult(b, scale);

  // Axis lines
  stroke(80);
  strokeWeight(1);
  line(-width, 0, width, 0);
  line(0, -height, 0, height);

  // Dynamic color based on dot sign
  let dotColor = color(120, 180, 255); // positive
  if (abs(dot) < 0.02) dotColor = color(255, 220, 120); // near zero
  if (dot < 0) dotColor = color(255, 120, 120); // negative

  drawArrow(av, color(120, 180, 255), 'A');
  drawArrow(bv, dotColor, 'B');

  // Arc showing theta
  noFill();
  stroke(230);
  strokeWeight(2);
  arc(0, 0, 80, 80, 0, b.heading());

  // HUD
  resetMatrix();
  fill(235);
  noStroke();
  textSize(16);
  text('Vector A = (1, 0)', 20, 30);
  text(`Vector B = (${b.x.toFixed(3)}, ${b.y.toFixed(3)})`, 20, 56);
  text(`dot(A, B) = ${dot.toFixed(3)}`, 20, 82);
  text(`theta = ${(degrees(theta)).toFixed(1)}°`, 20, 108);

  textSize(14);
  text('Blue = positive dot | Yellow = near zero | Red = negative dot', 20, 138);

  angle += 0.02;
}
</script>
```

## Why this animation is useful

As the vector `B` rotates:

- Near `0°`, `dot` approaches `1` (strong alignment).
- Near `90°`, `dot` approaches `0` (no directional alignment).
- Near `180°`, `dot` approaches `-1` (opposite direction).

This makes dot product intuition immediate and visual.

## Equivalent 3D interpretation

In 3D (`Vector3`), the same logic applies:

```text
dot = ax*bx + ay*by + az*bz
```

You can still think in terms of angle and alignment. The only difference is that vectors now move in three axes (x, y, z), which is typical for camera logic, AI vision cones, and lighting calculations.
