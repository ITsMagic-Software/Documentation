# UICheckBox

Controle de alternancia entre marcado e desmarcado ao toque.

## Criar no Editor

1. Garanta que existe um `UIController` na cena.
2. Crie um GameObject e adicione `UIRect`.
3. Adicione o componente `
UICheckBox
`.

## Como Usar

1. Pegue o componente com `myObject.findComponent(UICheckBox.class)`.
2. Leia e altere as propriedades do componente para controlar o comportamento.
3. Teste o input ou layout no modo Play.

## Exemplo em Java

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

## Notas

- Voce pode substituir imagens ou texturas no inspetor ou via codigo quando o componente suporta isso.

