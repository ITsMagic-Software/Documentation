# UIHoverButton

Botao com feedback de hover e clique para interacao mais rica.

## Criar no Editor

1. Garanta que existe um `UIController` na cena.
2. Crie um GameObject e adicione `UIRect`.
3. Adicione o componente `
UIHoverButton
`.

## Como Usar

1. Pegue o componente com `myObject.findComponent(UIHoverButton.class)`.
2. Leia e altere as propriedades do componente para controlar o comportamento.
3. Teste o input ou layout no modo Play.

## Exemplo em Java

```java
SpatialObject myObject = /* your object */;
UIHoverButton comp = myObject.findComponent(UIHoverButton.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the border value:
    comp.border = 1f;
    // read the border value:
    float borderValue = comp.border;
    // read the clicked value:
    boolean clickedValue = comp.clicked;

    // set the clickedColor value:
    comp.clickedColor = new Color(255, 255, 255, 255);
    // read the clickedColor value:
    Color clickedColorValue = comp.clickedColor;

    // set the clickedTexture value:
    comp.clickedTexture = tex;
    // read the clickedTexture value:
    Texture clickedTextureValue = comp.clickedTexture;
    // read the fontFile value:
    String fontFileValue = comp.fontFile;
    // read the hover value:
    boolean hoverValue = comp.hover;

    // set the hoverTexture value:
    comp.hoverTexture = tex;
    // read the hoverTexture value:
    Texture hoverTextureValue = comp.hoverTexture;
    // read the justBeginHover value:
    boolean justBeginHoverValue = comp.justBeginHover;

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

    // set the resolution value:
    comp.resolution = 1;
    // read the resolution value:
    int resolutionValue = comp.resolution;

    // set the text value:
    comp.text = "value";
    // read the text value:
    String textValue = comp.text;

    // set the textClickedColor value:
    comp.textClickedColor = new Color(255, 255, 255, 255);
    // read the textClickedColor value:
    Color textClickedColorValue = comp.textClickedColor;

    // set the textHoverColor value:
    comp.textHoverColor = new Color(255, 255, 255, 255);
    // read the textHoverColor value:
    Color textHoverColorValue = comp.textHoverColor;

    // set the textNormalColor value:
    comp.textNormalColor = new Color(255, 255, 255, 255);
    // read the textNormalColor value:
    Color textNormalColorValue = comp.textNormalColor;

    // set the textSize value:
    comp.textSize = 1f;
    // read the textSize value:
    float textSizeValue = comp.textSize;

}
```

## Notas

- Voce pode substituir imagens ou texturas no inspetor ou via codigo quando o componente suporta isso.

