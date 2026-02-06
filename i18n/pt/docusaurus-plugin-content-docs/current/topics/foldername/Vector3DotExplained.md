{@import ../../links.md}

# Vector3.dot explicado

`Vector3.dot` (produto escalar) mede o alinhamento direcional entre dois vetores 3D.

## Fórmula

Para vetores `a = (ax, ay, az)` e `b = (bx, by, bz)`:

```text
a · b = ax * bx + ay * by + az * bz
```

Se ambos estiverem normalizados (`|a| = 1` e `|b| = 1`):

```text
a · b = cos(theta)
```

`theta` é o ângulo entre os vetores.

## Significado do resultado

- `dot > 0`: vetores apontam majoritariamente na mesma direção.
- `dot = 0`: vetores são perpendiculares (`90°`).
- `dot < 0`: vetores apontam para direções opostas.
- `dot = 1`: mesma direção exata (caso normalizado).
- `dot = -1`: direção oposta exata (caso normalizado).

## Por que isso é útil em jogos

- **Checagem de campo de visão**: saber se um alvo está à frente de um NPC/câmera.
- **Iluminação (Lambert difuso)**: `max(0, normal · lightDir)`.
- **Alinhamento de movimento**: detectar se a entrada acompanha a direção do personagem.
- **Orientação de superfície**: identificar superfícies voltadas para cima/lado.

## Animação interativa (p5.js)

<iframe
  src="/htmls/vector3-dot-explained.html"
  title="Animação interativa do produto escalar Vector3"
  width="100%"
  height="460"
  style="border:1px solid #2f2f2f;border-radius:8px;background:#121212;"
  loading="lazy"
></iframe>

## Como interpretar a animação

- O vetor **A** fica fixo no eixo x.
- O vetor **B** gira ao redor da origem.
- O HUD mostra:
  - `dot(A, B)`
  - `theta` em graus.
- A cor indica o sinal:
  - **Azul**: positivo (alinhamento no mesmo lado)
  - **Amarelo**: próximo de zero (quase perpendicular)
  - **Vermelho**: negativo (direções opostas)

## Leitura passo a passo

Conforme `B` gira:

1. Perto de `0°`, os vetores alinham e `dot` se aproxima de `1`.
2. Perto de `90°`, ficam perpendiculares e `dot` se aproxima de `0`.
3. Perto de `180°`, ficam opostos e `dot` se aproxima de `-1`.

Isso gera uma intuição visual imediata de como direção e ângulo afetam o resultado do produto escalar.
