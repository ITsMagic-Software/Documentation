# UIImage

Renderiza uma textura ou sprite dentro do retangulo com tint.

## Criar no Editor

1. Garanta que existe um `UIController` na cena.
2. Crie um GameObject e adicione `UIRect`.
3. Adicione o componente `
UIImage
`.

## Como Usar

1. Pegue o componente com `myObject.findComponent(UIImage.class)`.
2. Leia e altere as propriedades do componente para controlar o comportamento.
3. Teste o input ou layout no modo Play.

## Exemplo em Java

```java
SpatialObject myObject = /* your object */;
UIImage comp = myObject.findComponent(UIImage.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the border value:
    comp.border = 1f;
    // read the border value:
    float borderValue = comp.border;

    // set the color value:
    comp.color = new Color(255, 255, 255, 255);
    // read the color value:
    Color colorValue = comp.color;

    // set the texture value:
    comp.texture = tex;
    // read the texture value:
    Texture textureValue = comp.texture;

}
```

