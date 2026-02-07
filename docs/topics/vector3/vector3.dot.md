# `Vector3.dot`

## Signature

```java
float dot(Vector3 v)
```

## Summary

Returns the dot product between this vector and another vector.

## Description

The dot product is useful for determining how similar two directions are. When both vectors are normalized:
- Returns 1 when vectors point in the same direction
- Returns 0 when vectors are perpendicular
- Returns -1 when vectors point in opposite directions

This is commonly used to check if an object is in front of or behind another object, or to measure the angle relationship between two directions.

## Example

```java
public SpatialObject object;

/// Run only once
void start() {}

/// Repeat every frame
void repeat() {
  Vector3 forward = myTransform.forward();
  Vector3 toTarget = (object.getPosition() - myTransform.getPosition()).normalize();
  float d = forward.dot(toTarget);

  if (d > 0.5f) {
    print("inFront");
  } else {
    print("inBack");
  }
}
```

## Return Value

**float**: The dot product of the two vectors.

## Common Usage Patterns

**Detecting direction**: Check if an object is in front of or behind using the forward vector.

```java
Vector3 forward = myTransform.forward();
Vector3 toObject = (target.getPosition() - myTransform.getPosition()).normalize();
float alignment = forward.dot(toObject);

if (alignment > 0) {
  print("Target is in front");
}
```

**Measuring alignment**: Determine how closely two vectors align.

```java
Vector3 moveDirection = velocity.normalize();
Vector3 desiredDirection = targetDirection.normalize();
float similarity = moveDirection.dot(desiredDirection);
```

**Field of view checks**: Combine with a threshold to create a vision cone.

```java
float viewAngle = forward.dot(toTarget);
if (viewAngle > 0.7f) {
  print("Within narrow field of view");
}
```

<div style={{ width: "100%", aspectRatio: "1 / 1" }}>
  <iframe
    src="/hpages/vector3.dot.vis.html"
    style={{ width: "100%", height: "100%", border: "none" }}
  />
</div>
