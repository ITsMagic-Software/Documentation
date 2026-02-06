# UIProgressBar

Displays a fill amount from 0 to 1 with optional background and handle visuals.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UIProgressBar
` component.

## How to Use

1. Get the component with `myObject.findComponent(UIProgressBar.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UIProgressBar comp = myObject.findComponent(UIProgressBar.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the backgroundColor value:
    comp.backgroundColor = new Color(255, 255, 255, 255);
    // read the backgroundColor value:
    Color backgroundColorValue = comp.backgroundColor;

    // set the backgroundTexture value:
    comp.backgroundTexture = tex;
    // read the backgroundTexture value:
    Texture backgroundTextureValue = comp.backgroundTexture;

    // set the border value:
    comp.border = 1f;
    // read the border value:
    float borderValue = comp.border;

    // set the handlerColor value:
    comp.handlerColor = new Color(255, 255, 255, 255);
    // read the handlerColor value:
    Color handlerColorValue = comp.handlerColor;

    // set the handlerTexture value:
    comp.handlerTexture = tex;
    // read the handlerTexture value:
    Texture handlerTextureValue = comp.handlerTexture;

    // set the jRPaddingBottom value:
    comp.jRPaddingBottom = 1;
    // read the jRPaddingBottom value:
    int jRPaddingBottomValue = comp.jRPaddingBottom;

    // set the jRPaddingLeft value:
    comp.jRPaddingLeft = 1;
    // read the jRPaddingLeft value:
    int jRPaddingLeftValue = comp.jRPaddingLeft;

    // set the jRPaddingRight value:
    comp.jRPaddingRight = 1;
    // read the jRPaddingRight value:
    int jRPaddingRightValue = comp.jRPaddingRight;

    // set the jRPaddingTop value:
    comp.jRPaddingTop = 1;
    // read the jRPaddingTop value:
    int jRPaddingTopValue = comp.jRPaddingTop;

    // set the orientation value:
    comp.orientation = Orientation.Horizontal;
    // read the orientation value:
    Orientation orientationValue = comp.orientation;

    // set the value value:
    comp.value = 1f;
    // read the value value:
    float valueValue = comp.value;

}
```

## Notes

- You can replace images or textures in the inspector or via code when the component supports it.

