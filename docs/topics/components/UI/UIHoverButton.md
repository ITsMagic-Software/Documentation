# UIHoverButton

Button that adds hover and click feedback states for richer interaction.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UIHoverButton
` component.

## How to Use

1. Get the component with `myObject.findComponent(UIHoverButton.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UIHoverButton comp = myObject.findComponent(UIHoverButton.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the border value:
    comp.border = 1f;
    // read the border value:
    float borderValue = comp.border;
    // read the clicked value:
    boolean clickedValue = comp.clicked;

    // set the clickedColor value:
    comp.clickedColor = new Color(255, 255, 255, 255);
    // read the clickedColor value:
    Color clickedColorValue = comp.clickedColor;

    // set the clickedTexture value:
    comp.clickedTexture = tex;
    // read the clickedTexture value:
    Texture clickedTextureValue = comp.clickedTexture;
    // read the fontFile value:
    String fontFileValue = comp.fontFile;
    // read the hover value:
    boolean hoverValue = comp.hover;

    // set the hoverTexture value:
    comp.hoverTexture = tex;
    // read the hoverTexture value:
    Texture hoverTextureValue = comp.hoverTexture;
    // read the justBeginHover value:
    boolean justBeginHoverValue = comp.justBeginHover;

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

    // set the resolution value:
    comp.resolution = 1;
    // read the resolution value:
    int resolutionValue = comp.resolution;

    // set the text value:
    comp.text = "value";
    // read the text value:
    String textValue = comp.text;

    // set the textClickedColor value:
    comp.textClickedColor = new Color(255, 255, 255, 255);
    // read the textClickedColor value:
    Color textClickedColorValue = comp.textClickedColor;

    // set the textHoverColor value:
    comp.textHoverColor = new Color(255, 255, 255, 255);
    // read the textHoverColor value:
    Color textHoverColorValue = comp.textHoverColor;

    // set the textNormalColor value:
    comp.textNormalColor = new Color(255, 255, 255, 255);
    // read the textNormalColor value:
    Color textNormalColorValue = comp.textNormalColor;

    // set the textSize value:
    comp.textSize = 1f;
    // read the textSize value:
    float textSizeValue = comp.textSize;

}
```

## Notes

- You can replace images or textures in the inspector or via code when the component supports it.

