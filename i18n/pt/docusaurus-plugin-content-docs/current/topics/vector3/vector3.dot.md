# `Vector3.dot`

## Assinatura

```java
float dot(Vector3 v)
```

## Resumo

Retorna o produto escalar entre este vetor e outro vetor.

## Descrição

O produto escalar é útil para determinar o grau de similaridade entre duas direções. Quando ambos os vetores são normalizados:

```java
public SpatialObject object;

/// Run only once
void start() {}

/// Repeat every frame
void repeat() {
  Vector3 forward = myTransform.forward();
  Vector3 toTarget = (object.getPosition() - myTransform.getPosition()).normalize();
  float d = forward.dot(toTarget);

  if (d > 0.5f) {
    print("inFront");
  } else {
    print("inBack");
  }
}
```

##

**float**: O produto escalar dos dois vetores.

## Padrões de Uso Comuns

**Detecção de direção**: Verifica se um objeto está à frente ou atrás usando o vetor de direção.

java
Vector3 forward = myTransform.forward();
Vector3 toObject = (target.getPosition() - myTransform.getPosition()).normalize();
float alignment = forward.dot(toObject);

if (alignment > 0) {
  print("Target is in front");
}
```

**Medindo o alinhamento**: Determine o quão próximos dois vetores estão alinhados.

```java
Vector3 moveDirection = velocity.normalize();
Vector3 desiredDirection = targetDirection.normalize();
float similarity = moveDirection.dot(desiredDirection);
```

**Verificações do campo de visão**: Combine com um limiar para criar um cone de visão.

```java
float viewAngle = forward.dot(toTarget);
if (viewAngle > 0.7f) {
  print("Within narrow field of view");
}
```
<div style={{ width: "100%", aspectRatio: "1 / 1" }}>
  <iframe
    src="/hpages/vector3.dot.vis.html"
    style={{ width: "100%", height: "100%", border: "none" }}
  />
</div>
