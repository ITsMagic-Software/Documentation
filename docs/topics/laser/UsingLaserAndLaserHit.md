{@import ../../links.md}

# Using Laser and LaserHit (Java)

The laser system behaves like a raycast: you shoot an invisible line and the engine tells you whether it hit something.
`Component` methods like `repeat()` run every frame, which makes lasers easy to use in gameplay logic that updates continuously.

## Example (beginner-friendly)

The example below creates a `Laser`, fires it inside `repeat()`, and handles the case where nothing is hit by catching `NoHitException`.

```java
public class LaserExample extends Component {
    private final Laser laser = new Laser();

    @Override
    public void repeat() {
        try {
            LaserHit hit = laser.trace(myObject.getGlobalPosition(), myObject.getForward());

            // Use the hit immediately (e.g., read hit point, collider, etc.).
            // This is where you react to the collision.
        } catch (NoHitException exception) {
            // Nothing was hit this frame. Decide what to do here.
        }
    }
}
```

## Why not store `LaserHit` globally?

For beginners, it may sound convenient to store the `LaserHit` in a global variable and use it later,
but that is **not a good practice** because the hit data can become outdated after the next frame.
Lasers are meant to be evaluated **per frame**, so you should use the hit right after you trace.

If you really need to keep it for later, always check if it exists:

```java
LaserHit cachedHit = null;

// Later...
if (cachedHit != null) {
    // Safe to use cachedHit
}
```

That `null` check prevents errors when no hit happened and ensures your code stays safe for beginners.
