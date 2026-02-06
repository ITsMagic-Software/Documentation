# UIInputText

Campo de texto editavel com caret, selecao e input do teclado.

## Criar no Editor

1. Garanta que existe um `UIController` na cena.
2. Crie um GameObject e adicione `UIRect`.
3. Adicione o componente `
UIInputText
`.

## Como Usar

1. Pegue o componente com `myObject.findComponent(UIInputText.class)`.
2. Leia e altere as propriedades do componente para controlar o comportamento.
3. Teste o input ou layout no modo Play.

## Exemplo em Java

```java
SpatialObject myObject = /* your object */;
UIInputText comp = myObject.findComponent(UIInputText.class);
if (comp != null) {
    // set the color value:
    comp.color = new Color(255, 255, 255, 255);
    // read the color value:
    Color colorValue = comp.color;

    // set the text value:
    comp.text = "value";
    // read the text value:
    String textValue = comp.text;

    // set the textSize value:
    comp.textSize = 1f;
    // read the textSize value:
    float textSizeValue = comp.textSize;

}
```

