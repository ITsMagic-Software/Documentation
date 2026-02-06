# UITouchTrigger

Low-level touch listener that exposes pressed/down/up states for custom UI logic.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UITouchTrigger
` component.

## How to Use

1. Get the component with `myObject.findComponent(UITouchTrigger.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UITouchTrigger comp = myObject.findComponent(UITouchTrigger.class);
if (comp != null) {
    // read the selectedTouch value:
    Touch selectedTouchValue = comp.selectedTouch;

}
```

