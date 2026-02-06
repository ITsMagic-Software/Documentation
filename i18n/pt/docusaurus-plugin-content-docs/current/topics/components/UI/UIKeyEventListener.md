# UIKeyEventListener

Recebe eventos de teclado para elementos de UI.

## Criar no Editor

1. Garanta que existe um `UIController` na cena.
2. Crie um GameObject e adicione `UIRect`.
3. Adicione o componente `
UIKeyEventListener
`.

## Como Usar

1. Pegue o componente com `myObject.findComponent(UIKeyEventListener.class)`.
2. Leia e altere as propriedades do componente para controlar o comportamento.
3. Teste o input ou layout no modo Play.

## Exemplo em Java

```java
SpatialObject myObject = /* your object */;
UIKeyEventListener comp = myObject.findComponent(UIKeyEventListener.class);
if (comp != null) {
    // set the keyName value:
    comp.keyName = "value";
    // read the keyName value:
    String keyNameValue = comp.keyName;

}
```

