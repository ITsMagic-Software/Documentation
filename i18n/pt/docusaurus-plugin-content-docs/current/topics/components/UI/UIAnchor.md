# UIAnchor

Ancora as bordas no pai para acompanhar resize e escala.

## Criar no Editor

1. Garanta que existe um `UIController` na cena.
2. Crie um GameObject e adicione `UIRect`.
3. Adicione o componente `
UIAnchor
`.

## Como Usar

1. Pegue o componente com `myObject.findComponent(UIAnchor.class)`.
2. Leia e altere as propriedades do componente para controlar o comportamento.
3. Teste o input ou layout no modo Play.

## Exemplo em Java

```java
SpatialObject myObject = /* your object */;
UIAnchor comp = myObject.findComponent(UIAnchor.class);
if (comp != null) {
    // set the bottomAnchor value:
    comp.bottomAnchor = new VerticalConstraintTarget();
    // read the bottomAnchor value:
    VerticalConstraintTarget bottomAnchorValue = comp.bottomAnchor;

    // set the bottomOffset value:
    comp.bottomOffset = 1;
    // read the bottomOffset value:
    int bottomOffsetValue = comp.bottomOffset;

    // set the bottomTarget value:
    comp.bottomTarget = new SpatialObject();
    // read the bottomTarget value:
    SpatialObject bottomTargetValue = comp.bottomTarget;

    // set the expandH value:
    comp.expandH = true;
    // read the expandH value:
    boolean expandHValue = comp.expandH;

    // set the expandW value:
    comp.expandW = true;
    // read the expandW value:
    boolean expandWValue = comp.expandW;

    // set the leftAnchor value:
    comp.leftAnchor = new HorizontalConstraintTarget();
    // read the leftAnchor value:
    HorizontalConstraintTarget leftAnchorValue = comp.leftAnchor;

    // set the leftOffset value:
    comp.leftOffset = 1;
    // read the leftOffset value:
    int leftOffsetValue = comp.leftOffset;

    // set the leftTarget value:
    comp.leftTarget = new SpatialObject();
    // read the leftTarget value:
    SpatialObject leftTargetValue = comp.leftTarget;

    // set the rightAnchor value:
    comp.rightAnchor = new HorizontalConstraintTarget();
    // read the rightAnchor value:
    HorizontalConstraintTarget rightAnchorValue = comp.rightAnchor;

    // set the rightOffset value:
    comp.rightOffset = 1;
    // read the rightOffset value:
    int rightOffsetValue = comp.rightOffset;

    // set the rightTarget value:
    comp.rightTarget = new SpatialObject();
    // read the rightTarget value:
    SpatialObject rightTargetValue = comp.rightTarget;

    // set the topAnchor value:
    comp.topAnchor = new VerticalConstraintTarget();
    // read the topAnchor value:
    VerticalConstraintTarget topAnchorValue = comp.topAnchor;

    // set the topOffset value:
    comp.topOffset = 1;
    // read the topOffset value:
    int topOffsetValue = comp.topOffset;

    // set the topTarget value:
    comp.topTarget = new SpatialObject();
    // read the topTarget value:
    SpatialObject topTargetValue = comp.topTarget;

}
```

