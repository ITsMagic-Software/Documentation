# UIRotateImage

Renders an image with rotation around its center for dials, needles, and spinners.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UIRotateImage
` component.

## How to Use

1. Get the component with `myObject.findComponent(UIRotateImage.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UIRotateImage comp = myObject.findComponent(UIRotateImage.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the angle value:
    comp.angle = 1f;
    // read the angle value:
    float angleValue = comp.angle;

    // set the texture value:
    comp.texture = tex;
    // read the texture value:
    Texture textureValue = comp.texture;

}
```

