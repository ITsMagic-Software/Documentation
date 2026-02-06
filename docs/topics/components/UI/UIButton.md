# UIButton

Interactive button that renders text and supports normal/pressed visuals plus touch states.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UIButton
` component.

## How to Use

1. Get the component with `myObject.findComponent(UIButton.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UIButton comp = myObject.findComponent(UIButton.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the border value:
    comp.border = 1f;
    // read the border value:
    float borderValue = comp.border;
    // read the down value:
    boolean downValue = comp.down;
    // read the fontFile value:
    String fontFileValue = comp.fontFile;

    // set the normalColor value:
    comp.normalColor = new Color(255, 255, 255, 255);
    // read the normalColor value:
    Color normalColorValue = comp.normalColor;

    // set the normalTexture value:
    comp.normalTexture = tex;
    // read the normalTexture value:
    Texture normalTextureValue = comp.normalTexture;

    // set the padding value:
    comp.padding = new Vector2(1, 1);
    // read the padding value:
    Vector2 paddingValue = comp.padding;
    // read the pressed value:
    boolean pressedValue = comp.pressed;

    // set the pressedColor value:
    comp.pressedColor = new Color(255, 255, 255, 255);
    // read the pressedColor value:
    Color pressedColorValue = comp.pressedColor;

    // set the pressedTexture value:
    comp.pressedTexture = tex;
    // read the pressedTexture value:
    Texture pressedTextureValue = comp.pressedTexture;

    // set the resolution value:
    comp.resolution = 1;
    // read the resolution value:
    int resolutionValue = comp.resolution;

    // set the text value:
    comp.text = "value";
    // read the text value:
    String textValue = comp.text;

    // set the textNormalColor value:
    comp.textNormalColor = new Color(255, 255, 255, 255);
    // read the textNormalColor value:
    Color textNormalColorValue = comp.textNormalColor;

    // set the textPressedColor value:
    comp.textPressedColor = new Color(255, 255, 255, 255);
    // read the textPressedColor value:
    Color textPressedColorValue = comp.textPressedColor;

    // set the textSize value:
    comp.textSize = 1f;
    // read the textSize value:
    float textSizeValue = comp.textSize;
    // read the up value:
    boolean upValue = comp.up;

}
```

## Notes

- You can replace images or textures in the inspector or via code when the component supports it.

