# UI Widgets: CheckBox, RadioButton, RadioGroup, DrivingWheel

This topic shows how to use the new UI widgets in the editor and in Java code.

## Create in the Editor

1. Topbar -> Create Object -> UI -> Widgets -> Check box
2. Topbar -> Create Object -> UI -> Widgets -> Radio group
3. Topbar -> Create Object -> UI -> Widgets -> Driving wheel

The Radio group instantiator creates a `UIRadioGroup` with a `UIVerticalLayout` and two `UIRadioButton` children.

## Theme Images

The default theme provides checkbox and radio textures. You can replace the theme images or override them per component through the inspector or via code.

## Java Usage

### UICheckBox

```java
SpatialObject myObject = /* your object */;
UICheckBox comp = myObject.findComponent(UICheckBox.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the checked value:
    comp.checked = true;
    // read the checked value:
    boolean checkedValue = comp.checked;
    // read the pressed value:
    boolean pressedValue = comp.pressed;
    // read the down value:
    boolean downValue = comp.down;
    // read the up value:
    boolean upValue = comp.up;

    // set the color value:
    comp.color = new Color(255, 255, 255, 255);
    // read the color value:
    Color colorValue = comp.color;

    // set the checkedTexture value:
    comp.checkedTexture = tex;
    // read the checkedTexture value:
    Texture checkedTextureValue = comp.checkedTexture;

    // set the uncheckedTexture value:
    comp.uncheckedTexture = tex;
    // read the uncheckedTexture value:
    Texture uncheckedTextureValue = comp.uncheckedTexture;

}
```

### UIRadioGroup

```java
SpatialObject myObject = /* your object */;
UIRadioGroup comp = myObject.findComponent(UIRadioGroup.class);
if (comp != null) {
}
```

### UIRadioButton

```java
SpatialObject myObject = /* your object */;
UIRadioButton comp = myObject.findComponent(UIRadioButton.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the checked value:
    comp.checked = true;
    // read the checked value:
    boolean checkedValue = comp.checked;
    // read the pressed value:
    boolean pressedValue = comp.pressed;
    // read the down value:
    boolean downValue = comp.down;
    // read the up value:
    boolean upValue = comp.up;

    // set the color value:
    comp.color = new Color(255, 255, 255, 255);
    // read the color value:
    Color colorValue = comp.color;

    // set the checkedTexture value:
    comp.checkedTexture = tex;
    // read the checkedTexture value:
    Texture checkedTextureValue = comp.checkedTexture;

    // set the uncheckedTexture value:
    comp.uncheckedTexture = tex;
    // read the uncheckedTexture value:
    Texture uncheckedTextureValue = comp.uncheckedTexture;

}
```

### UIDrivingWheel

```java
SpatialObject myObject = /* your object */;
UIDrivingWheel comp = myObject.findComponent(UIDrivingWheel.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // read the value value:
    float valueValue = comp.value;
    // read the angle value:
    float angleValue = comp.angle;

    // set the lerp value:
    comp.lerp = 1f;
    // read the lerp value:
    float lerpValue = comp.lerp;

    // set the maxAngle value:
    comp.maxAngle = 1f;
    // read the maxAngle value:
    float maxAngleValue = comp.maxAngle;
    // read the pressed value:
    boolean pressedValue = comp.pressed;
    // read the down value:
    boolean downValue = comp.down;
    // read the up value:
    boolean upValue = comp.up;

    // set the color value:
    comp.color = new Color(255, 255, 255, 255);
    // read the color value:
    Color colorValue = comp.color;

    // set the texture value:
    comp.texture = tex;
    // read the texture value:
    Texture textureValue = comp.texture;

}
```

## Tips

- The checkbox toggles on `down` to avoid the first-frame `up` event.
- `UIDrivingWheel` uses touch input to set a continuous axis value.

