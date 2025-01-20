# Zombie-smash

## Development setup

### Nix

```bash
nix develop [--command <shell>]
```

### Others

1. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/).
2. Run `uv run src/main.py` to run the game.

## Design

### Sprite map

- A `SpriteMap` is simply a list of `pygame.Surface`, which is a preloaded list of images.
- An index into the `SpriteMap` represents an image to be rendered.

### Animation

Most effort are spent abstracting out animations:
- `Animation`: Simply a sequence of indexes into the `SpriteMap`, which can loop (`should_loop`)
- `AnimationSet`: A sequence of animations. A game object's state can be shown as a combination of multiple animations, for example *zombie spawning* can be (1) digging a hole and appear (2) shifting left and right (loop).
- `Animatable`: An animatable game object, which can switch between animation sets, depending on its state. Each state of the game object has a corresponding method to switch to the corresponding animation set. For example, `NormalZombie`'s `spawn`, `despawn` or `kill`. An `Animatable` knows its current time (so that it can determine which frame in the `AnimationSet` to draw) and can draw itself.

### Static

A static game object is represented by the `Static` class, which knows about its position and can draw itself.
