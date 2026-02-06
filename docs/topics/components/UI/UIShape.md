# UIShape

Draws basic UI shapes (rectangles, circles, lines) with color and size settings.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UIShape
` component.

## How to Use

1. Get the component with `myObject.findComponent(UIShape.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UIShape comp = myObject.findComponent(UIShape.class);
if (comp != null) {
    // set the bottomLeftCorner value:
    comp.bottomLeftCorner = new CornerType();
    // read the bottomLeftCorner value:
    CornerType bottomLeftCornerValue = comp.bottomLeftCorner;

    // set the bottomRightCorner value:
    comp.bottomRightCorner = new CornerType();
    // read the bottomRightCorner value:
    CornerType bottomRightCornerValue = comp.bottomRightCorner;

    // set the color value:
    comp.color = new Color(255, 255, 255, 255);
    // read the color value:
    Color colorValue = comp.color;

    // set the colorGradient value:
    comp.colorGradient = new ColorGradient();
    // read the colorGradient value:
    ColorGradient colorGradientValue = comp.colorGradient;

    // set the corner value:
    comp.corner = 1f;
    // read the corner value:
    float cornerValue = comp.corner;

    // set the gradientAngle value:
    comp.gradientAngle = 1f;
    // read the gradientAngle value:
    float gradientAngleValue = comp.gradientAngle;

    // set the gradientMode value:
    comp.gradientMode = new GradientMode();
    // read the gradientMode value:
    GradientMode gradientModeValue = comp.gradientMode;

    // set the hole value:
    comp.hole = 1f;
    // read the hole value:
    float holeValue = comp.hole;

    // set the innerGlowColor value:
    comp.innerGlowColor = new Color(255, 255, 255, 255);
    // read the innerGlowColor value:
    Color innerGlowColorValue = comp.innerGlowColor;

    // set the innerGlowSize value:
    comp.innerGlowSize = 1f;
    // read the innerGlowSize value:
    float innerGlowSizeValue = comp.innerGlowSize;

    // set the innerGlowSmooth value:
    comp.innerGlowSmooth = 1f;
    // read the innerGlowSmooth value:
    float innerGlowSmoothValue = comp.innerGlowSmooth;

    // set the innerShadowAngle value:
    comp.innerShadowAngle = 1f;
    // read the innerShadowAngle value:
    float innerShadowAngleValue = comp.innerShadowAngle;

    // set the innerShadowColor value:
    comp.innerShadowColor = new Color(255, 255, 255, 255);
    // read the innerShadowColor value:
    Color innerShadowColorValue = comp.innerShadowColor;

    // set the innerShadowSize value:
    comp.innerShadowSize = 1f;
    // read the innerShadowSize value:
    float innerShadowSizeValue = comp.innerShadowSize;

    // set the innerShadowSmooth value:
    comp.innerShadowSmooth = 1f;
    // read the innerShadowSmooth value:
    float innerShadowSmoothValue = comp.innerShadowSmooth;

    // set the maskAngle value:
    comp.maskAngle = 1f;
    // read the maskAngle value:
    float maskAngleValue = comp.maskAngle;

    // set the maskMode value:
    comp.maskMode = new MaskMode();
    // read the maskMode value:
    MaskMode maskModeValue = comp.maskMode;

    // set the maskValue value:
    comp.maskValue = 1f;
    // read the maskValue value:
    float maskValueValue = comp.maskValue;

    // set the outerGlowColor value:
    comp.outerGlowColor = new Color(255, 255, 255, 255);
    // read the outerGlowColor value:
    Color outerGlowColorValue = comp.outerGlowColor;

    // set the outerGlowSize value:
    comp.outerGlowSize = 1f;
    // read the outerGlowSize value:
    float outerGlowSizeValue = comp.outerGlowSize;

    // set the outerGlowSmooth value:
    comp.outerGlowSmooth = 1f;
    // read the outerGlowSmooth value:
    float outerGlowSmoothValue = comp.outerGlowSmooth;

    // set the outerShadowAngle value:
    comp.outerShadowAngle = 1f;
    // read the outerShadowAngle value:
    float outerShadowAngleValue = comp.outerShadowAngle;

    // set the outerShadowColor value:
    comp.outerShadowColor = new Color(255, 255, 255, 255);
    // read the outerShadowColor value:
    Color outerShadowColorValue = comp.outerShadowColor;

    // set the outerShadowSize value:
    comp.outerShadowSize = 1f;
    // read the outerShadowSize value:
    float outerShadowSizeValue = comp.outerShadowSize;

    // set the outerShadowSmooth value:
    comp.outerShadowSmooth = 1f;
    // read the outerShadowSmooth value:
    float outerShadowSmoothValue = comp.outerShadowSmooth;

    // set the quality value:
    comp.quality = 1f;
    // read the quality value:
    float qualityValue = comp.quality;

    // set the stroke value:
    comp.stroke = 1f;
    // read the stroke value:
    float strokeValue = comp.stroke;

    // set the strokeColor value:
    comp.strokeColor = new Color(255, 255, 255, 255);
    // read the strokeColor value:
    Color strokeColorValue = comp.strokeColor;

    // set the topLeftCorner value:
    comp.topLeftCorner = new CornerType();
    // read the topLeftCorner value:
    CornerType topLeftCornerValue = comp.topLeftCorner;

    // set the topRightCorner value:
    comp.topRightCorner = new CornerType();
    // read the topRightCorner value:
    CornerType topRightCornerValue = comp.topRightCorner;

}
```

