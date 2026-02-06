# UIRotateImage

Renderiza imagem com rotacao no centro para ponteiros e mostradores.

## Criar no Editor

1. Garanta que existe um `UIController` na cena.
2. Crie um GameObject e adicione `UIRect`.
3. Adicione o componente `
UIRotateImage
`.

## Como Usar

1. Pegue o componente com `myObject.findComponent(UIRotateImage.class)`.
2. Leia e altere as propriedades do componente para controlar o comportamento.
3. Teste o input ou layout no modo Play.

## Exemplo em Java

```java
SpatialObject myObject = /* your object */;
UIRotateImage comp = myObject.findComponent(UIRotateImage.class);
if (comp != null) {
    Texture tex = /* load texture */ null;
    // set the angle value:
    comp.angle = 1f;
    // read the angle value:
    float angleValue = comp.angle;

    // set the texture value:
    comp.texture = tex;
    // read the texture value:
    Texture textureValue = comp.texture;

}
```

