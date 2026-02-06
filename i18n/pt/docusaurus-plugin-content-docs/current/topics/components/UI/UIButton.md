# UIButton

Botao interativo que renderiza texto e tem estado normal/pressionado.

## Criar no Editor

1. Garanta que existe um `UIController` na cena.
2. Crie um GameObject e adicione `UIRect`.
3. Adicione o componente `
UIButton
`.

## Como Usar

1. Pegue o componente com `myObject.findComponent(UIButton.class)`.
2. Leia e altere as propriedades do componente para controlar o comportamento.
3. Teste o input ou layout no modo Play.

## Exemplo em Java

```java
SpatialObject myObject = /* your object */;
UIButton comp = myObject.findComponent(UIButton.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the border value:
    comp.border = 1f;
    // read the border value:
    float borderValue = comp.border;
    // read the down value:
    boolean downValue = comp.down;
    // read the fontFile value:
    String fontFileValue = comp.fontFile;

    // set the normalColor value:
    comp.normalColor = new Color(255, 255, 255, 255);
    // read the normalColor value:
    Color normalColorValue = comp.normalColor;

    // set the normalTexture value:
    comp.normalTexture = tex;
    // read the normalTexture value:
    Texture normalTextureValue = comp.normalTexture;

    // set the padding value:
    comp.padding = new Vector2(1, 1);
    // read the padding value:
    Vector2 paddingValue = comp.padding;
    // read the pressed value:
    boolean pressedValue = comp.pressed;

    // set the pressedColor value:
    comp.pressedColor = new Color(255, 255, 255, 255);
    // read the pressedColor value:
    Color pressedColorValue = comp.pressedColor;

    // set the pressedTexture value:
    comp.pressedTexture = tex;
    // read the pressedTexture value:
    Texture pressedTextureValue = comp.pressedTexture;

    // set the resolution value:
    comp.resolution = 1;
    // read the resolution value:
    int resolutionValue = comp.resolution;

    // set the text value:
    comp.text = "value";
    // read the text value:
    String textValue = comp.text;

    // set the textNormalColor value:
    comp.textNormalColor = new Color(255, 255, 255, 255);
    // read the textNormalColor value:
    Color textNormalColorValue = comp.textNormalColor;

    // set the textPressedColor value:
    comp.textPressedColor = new Color(255, 255, 255, 255);
    // read the textPressedColor value:
    Color textPressedColorValue = comp.textPressedColor;

    // set the textSize value:
    comp.textSize = 1f;
    // read the textSize value:
    float textSizeValue = comp.textSize;
    // read the up value:
    boolean upValue = comp.up;

}
```

## Notas

- Voce pode substituir imagens ou texturas no inspetor ou via codigo quando o componente suporta isso.

