# UITouchTrigger

Listener de toque de baixo nivel com estados pressed/down/up.

## Criar no Editor

1. Garanta que existe um `UIController` na cena.
2. Crie um GameObject e adicione `UIRect`.
3. Adicione o componente `
UITouchTrigger
`.

## Como Usar

1. Pegue o componente com `myObject.findComponent(UITouchTrigger.class)`.
2. Leia e altere as propriedades do componente para controlar o comportamento.
3. Teste o input ou layout no modo Play.

## Exemplo em Java

```java
SpatialObject myObject = /* your object */;
UITouchTrigger comp = myObject.findComponent(UITouchTrigger.class);
if (comp != null) {
    // read the selectedTouch value:
    Touch selectedTouchValue = comp.selectedTouch;

}
```

