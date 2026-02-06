# UIProgressBar

Exibe progresso de 0 a 1 com fundo e preenchimento opcionais.

## Criar no Editor

1. Garanta que existe um `UIController` na cena.
2. Crie um GameObject e adicione `UIRect`.
3. Adicione o componente `
UIProgressBar
`.

## Como Usar

1. Pegue o componente com `myObject.findComponent(UIProgressBar.class)`.
2. Leia e altere as propriedades do componente para controlar o comportamento.
3. Teste o input ou layout no modo Play.

## Exemplo em Java

```java
SpatialObject myObject = /* your object */;
UIProgressBar comp = myObject.findComponent(UIProgressBar.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the backgroundColor value:
    comp.backgroundColor = new Color(255, 255, 255, 255);
    // read the backgroundColor value:
    Color backgroundColorValue = comp.backgroundColor;

    // set the backgroundTexture value:
    comp.backgroundTexture = tex;
    // read the backgroundTexture value:
    Texture backgroundTextureValue = comp.backgroundTexture;

    // set the border value:
    comp.border = 1f;
    // read the border value:
    float borderValue = comp.border;

    // set the handlerColor value:
    comp.handlerColor = new Color(255, 255, 255, 255);
    // read the handlerColor value:
    Color handlerColorValue = comp.handlerColor;

    // set the handlerTexture value:
    comp.handlerTexture = tex;
    // read the handlerTexture value:
    Texture handlerTextureValue = comp.handlerTexture;

    // set the jRPaddingBottom value:
    comp.jRPaddingBottom = 1;
    // read the jRPaddingBottom value:
    int jRPaddingBottomValue = comp.jRPaddingBottom;

    // set the jRPaddingLeft value:
    comp.jRPaddingLeft = 1;
    // read the jRPaddingLeft value:
    int jRPaddingLeftValue = comp.jRPaddingLeft;

    // set the jRPaddingRight value:
    comp.jRPaddingRight = 1;
    // read the jRPaddingRight value:
    int jRPaddingRightValue = comp.jRPaddingRight;

    // set the jRPaddingTop value:
    comp.jRPaddingTop = 1;
    // read the jRPaddingTop value:
    int jRPaddingTopValue = comp.jRPaddingTop;

    // set the orientation value:
    comp.orientation = Orientation.Horizontal;
    // read the orientation value:
    Orientation orientationValue = comp.orientation;

    // set the value value:
    comp.value = 1f;
    // read the value value:
    float valueValue = comp.value;

}
```

## Notas

- Voce pode substituir imagens ou texturas no inspetor ou via codigo quando o componente suporta isso.

