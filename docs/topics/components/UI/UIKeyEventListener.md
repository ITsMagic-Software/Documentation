# UIKeyEventListener

Receives keyboard input events for UI elements.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UIKeyEventListener
` component.

## How to Use

1. Get the component with `myObject.findComponent(UIKeyEventListener.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UIKeyEventListener comp = myObject.findComponent(UIKeyEventListener.class);
if (comp != null) {
    // set the keyName value:
    comp.keyName = "value";
    // read the keyName value:
    String keyNameValue = comp.keyName;

}
```

