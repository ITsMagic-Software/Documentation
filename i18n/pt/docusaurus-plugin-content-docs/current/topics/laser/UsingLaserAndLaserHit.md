{@import ../../links.md}

# Usando Laser e LaserHit (Java)

O sistema de laser se comporta como um raycast: você dispara uma linha invisível e o motor informa se ela atingiu algo.
Métodos de `Component` como `repeat()` rodam a cada frame, o que torna os lasers fáceis de usar em lógicas de jogo que atualizam continuamente.

## Exemplo (para iniciantes)

O exemplo abaixo cria um `Laser`, dispara dentro de `repeat()` e trata o caso em que nada é atingido capturando `NoHitException`.

```java
public class LaserExample extends Component {
    private final Laser laser = new Laser();

    @Override
    public void repeat() {
        try {
            LaserHit hit = laser.trace(myObject.getGlobalPosition(), myObject.getForward());

            // Use o hit imediatamente (ex.: ler ponto de impacto, collider, etc.).
            // Aqui é onde você reage à colisão.
        } catch (NoHitException exception) {
            // Nada foi atingido neste frame. Decida o que fazer aqui.
        }
    }
}
```

## Por que não armazenar `LaserHit` globalmente?

Para iniciantes, pode parecer conveniente guardar o `LaserHit` em uma variável global e usar depois,
mas isso **não é uma boa prática** porque os dados do hit podem ficar desatualizados após o próximo frame.
Lasers devem ser avaliados **por frame**, então você deve usar o hit logo após o trace.

Se você realmente precisar guardar para usar depois, sempre verifique se existe:

```java
LaserHit cachedHit = null;

// Depois...
if (cachedHit != null) {
    // Seguro usar cachedHit
}
```

Essa verificação de `null` evita erros quando nenhum hit aconteceu e mantém seu código seguro para iniciantes.
