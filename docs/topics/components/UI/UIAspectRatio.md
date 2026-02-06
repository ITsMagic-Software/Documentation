# UIAspectRatio

Locks width/height ratio to prevent stretching of UI elements.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UIAspectRatio
` component.

## How to Use

1. Get the component with `myObject.findComponent(UIAspectRatio.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UIAspectRatio comp = myObject.findComponent(UIAspectRatio.class);
if (comp != null) {
    // set the mode value:
    comp.mode = new Mode();
    // read the mode value:
    Mode modeValue = comp.mode;

    // set the proportion value:
    comp.proportion = 1f;
    // read the proportion value:
    float proportionValue = comp.proportion;

}
```

