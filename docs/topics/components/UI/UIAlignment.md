# UIAlignment

Aligns a UI element within its parent using horizontal and vertical alignment rules.

## Create in the Editor

1. Ensure there is a `UIController` in the scene.
2. Create a GameObject and add `UIRect`.
3. Add the `
UIAlignment
` component.

## How to Use

1. Get the component with `myObject.findComponent(UIAlignment.class)`.
2. Read and write the component properties to control behavior.
3. Test input or layout in Play mode.

## Java Example

```java
SpatialObject myObject = /* your object */;
UIAlignment comp = myObject.findComponent(UIAlignment.class);
if (comp != null) {
    // set the bottomCenterEnabled value:
    comp.bottomCenterEnabled = true;
    // read the bottomCenterEnabled value:
    boolean bottomCenterEnabledValue = comp.bottomCenterEnabled;

    // set the bottomLeftEnabled value:
    comp.bottomLeftEnabled = true;
    // read the bottomLeftEnabled value:
    boolean bottomLeftEnabledValue = comp.bottomLeftEnabled;

    // set the bottomRightEnabled value:
    comp.bottomRightEnabled = true;
    // read the bottomRightEnabled value:
    boolean bottomRightEnabledValue = comp.bottomRightEnabled;

    // set the centerEnabled value:
    comp.centerEnabled = true;
    // read the centerEnabled value:
    boolean centerEnabledValue = comp.centerEnabled;

    // set the centerLeftEnabled value:
    comp.centerLeftEnabled = true;
    // read the centerLeftEnabled value:
    boolean centerLeftEnabledValue = comp.centerLeftEnabled;

    // set the centerRightEnabled value:
    comp.centerRightEnabled = true;
    // read the centerRightEnabled value:
    boolean centerRightEnabledValue = comp.centerRightEnabled;

    // set the topCenterEnabled value:
    comp.topCenterEnabled = true;
    // read the topCenterEnabled value:
    boolean topCenterEnabledValue = comp.topCenterEnabled;

    // set the topLeftEnabled value:
    comp.topLeftEnabled = true;
    // read the topLeftEnabled value:
    boolean topLeftEnabledValue = comp.topLeftEnabled;

    // set the topRightEnabled value:
    comp.topRightEnabled = true;
    // read the topRightEnabled value:
    boolean topRightEnabledValue = comp.topRightEnabled;

}
```

