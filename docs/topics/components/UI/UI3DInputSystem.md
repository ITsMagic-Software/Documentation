# UI3DInputSystem

Enables UI interaction on 3D UI surfaces using screen touch mapping.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UI3DInputSystem
` component.

## How to Use

1. Get the component with `myObject.findComponent(UI3DInputSystem.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UI3DInputSystem comp = myObject.findComponent(UI3DInputSystem.class);
if (comp != null) {
    // set the maxHitDistance value:
    comp.maxHitDistance = 1f;
    // read the maxHitDistance value:
    float maxHitDistanceValue = comp.maxHitDistance;

}
```

