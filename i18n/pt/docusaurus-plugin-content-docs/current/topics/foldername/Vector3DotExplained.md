{@import ../../links.md}

# Vector3.dot explicado

`Vector3.dot` (produto escalar) mede o quanto dois vetores estão alinhados.

```text
a · b = ax * bx + ay * by + az * bz
```

Quando os vetores estão normalizados, o resultado é o cosseno do ângulo entre eles:

```text
a · b = cos(theta)
```

- `dot > 0`: direção parecida.
- `dot = 0`: perpendicular.
- `dot < 0`: direção oposta.

## Animação interativa (p5.js)

<iframe
  src="/htmls/vector3-dot-explained.html"
  title="Animação interativa do produto escalar Vector3"
  width="100%"
  height="460"
  style={{ border: '1px solid #2f2f2f', borderRadius: '8px', background: '#121212' }}
  loading="lazy"
/>

## Como interpretar a animação

- O vetor **A** é fixo.
- O vetor **B** gira continuamente.
- O HUD mostra os valores em tempo real de `dot(A, B)` e `theta`.
- As cores indicam o sinal:
  - Azul: dot positivo.
  - Amarelo: próximo de zero.
  - Vermelho: dot negativo.

## Casos de uso comuns em jogos

- Checagem de cone de visão / campo de visão.
- Cálculos de iluminação com normais de superfície.
- Verificação de direção em IA e validação de alvo.
- Alinhamento de movimento e filtros direcionais.
