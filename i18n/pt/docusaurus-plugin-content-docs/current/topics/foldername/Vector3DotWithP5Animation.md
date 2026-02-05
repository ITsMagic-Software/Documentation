{@import ../../links.md}

# Vector3.dot explicado com animação em p5.js

`Vector3.dot` (produto escalar) é uma das operações mais úteis de matemática 3D para jogos e gráficos interativos. Ele ajuda a medir **o quanto um vetor aponta na mesma direção de outro**.

## O que `Vector3.dot` faz

Dado dois vetores `a` e `b`:

```text
a · b = ax * bx + ay * by + az * bz
```

Se ambos os vetores estiverem normalizados (comprimento `1`), então:

```text
a · b = cos(theta)
```

Onde `theta` é o ângulo entre eles.

## Como interpretar o resultado

- `dot > 0`: os vetores apontam para direções parecidas.
- `dot = 0`: os vetores são perpendiculares (90°).
- `dot < 0`: os vetores apontam para direções opostas.
- `dot = 1`: exatamente a mesma direção (se normalizados).
- `dot = -1`: exatamente a direção oposta (se normalizados).

## Casos de uso práticos

- **Checagem de campo de visão** (o alvo está à frente do personagem/câmera?).
- **Iluminação** (Lambert difuso: normal · lightDirection).
- **Alinhamento de entrada** (o movimento está alinhado com a direção do personagem?).
- **Teste de superfícies** (uma superfície está virada para cima, para baixo ou para o lado?).

## Ideia de animação com p5.js

A animação abaixo gira um vetor ao redor da origem enquanto outro fica fixo. Ela mostra:

1. Os dois vetores.
2. O ângulo entre eles.
3. O valor do produto escalar atualizado a cada frame.
4. Uma dica de cor para valores positivos/zero/negativos.

```html
<script src="https://cdn.jsdelivr.net/npm/p5@1.9.3/lib/p5.min.js"></script>
<script>
let angle = 0;

function setup() {
  createCanvas(700, 420);
  textFont('monospace');
}

function drawArrow(v, col, label) {
  push();
  stroke(col);
  fill(col);
  strokeWeight(3);
  line(0, 0, v.x, v.y);

  // Ponta da seta
  push();
  translate(v.x, v.y);
  rotate(v.heading());
  triangle(0, 0, -12, 6, -12, -6);
  pop();

  noStroke();
  text(label, v.x + 8, v.y + 8);
  pop();
}

function draw() {
  background(18);
  translate(width * 0.5, height * 0.55);

  // Vetor A fixo (normalizado)
  const a = createVector(1, 0);

  // Vetor B rotacionando (normalizado)
  const b = createVector(cos(angle), sin(angle));

  // Produto escalar e ângulo
  const dot = a.dot(b);           // no intervalo [-1, 1]
  const theta = acos(constrain(dot, -1, 1));

  // Escala dos vetores para visualização
  const scale = 140;
  const av = p5.Vector.mult(a, scale);
  const bv = p5.Vector.mult(b, scale);

  // Eixos
  stroke(80);
  strokeWeight(1);
  line(-width, 0, width, 0);
  line(0, -height, 0, height);

  // Cor dinâmica baseada no sinal do dot
  let dotColor = color(120, 180, 255); // positivo
  if (abs(dot) < 0.02) dotColor = color(255, 220, 120); // perto de zero
  if (dot < 0) dotColor = color(255, 120, 120); // negativo

  drawArrow(av, color(120, 180, 255), 'A');
  drawArrow(bv, dotColor, 'B');

  // Arco mostrando theta
  noFill();
  stroke(230);
  strokeWeight(2);
  arc(0, 0, 80, 80, 0, b.heading());

  // HUD
  resetMatrix();
  fill(235);
  noStroke();
  textSize(16);
  text('Vector A = (1, 0)', 20, 30);
  text(`Vector B = (${b.x.toFixed(3)}, ${b.y.toFixed(3)})`, 20, 56);
  text(`dot(A, B) = ${dot.toFixed(3)}`, 20, 82);
  text(`theta = ${(degrees(theta)).toFixed(1)}°`, 20, 108);

  textSize(14);
  text('Azul = dot positivo | Amarelo = perto de zero | Vermelho = dot negativo', 20, 138);

  angle += 0.02;
}
</script>
```

## Por que essa animação é útil

Conforme o vetor `B` gira:

- Perto de `0°`, `dot` se aproxima de `1` (alinhamento forte).
- Perto de `90°`, `dot` se aproxima de `0` (sem alinhamento direcional).
- Perto de `180°`, `dot` se aproxima de `-1` (direção oposta).

Isso torna a intuição do produto escalar imediata e visual.

## Interpretação equivalente em 3D

No 3D (`Vector3`), a mesma lógica vale:

```text
dot = ax*bx + ay*by + az*bz
```

Você ainda pode pensar em termos de ângulo e alinhamento. A única diferença é que os vetores agora se movem em três eixos (x, y, z), algo comum em lógica de câmera, cone de visão de IA e cálculos de iluminação.
