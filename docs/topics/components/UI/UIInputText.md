# UIInputText

Editable text field with caret, selection, and keyboard input handling.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UIInputText
` component.

## How to Use

1. Get the component with `myObject.findComponent(UIInputText.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UIInputText comp = myObject.findComponent(UIInputText.class);
if (comp != null) {
    // set the color value:
    comp.color = new Color(255, 255, 255, 255);
    // read the color value:
    Color colorValue = comp.color;

    // set the text value:
    comp.text = "value";
    // read the text value:
    String textValue = comp.text;

    // set the textSize value:
    comp.textSize = 1f;
    // read the textSize value:
    float textSizeValue = comp.textSize;

}
```

