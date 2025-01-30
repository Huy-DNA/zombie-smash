# Zombie-smash

This is the first of the more formal tries at `pygame`, because of school projects ;).

## Development setup

### Nix

```bash
nix develop [--command <shell>]
```

### Others

1. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/).
2. Run `uv run src/main.py` to run the game.

## References

Some good `pygame` references:
  - What `pygame` is & its inception & philosophy: [pygame doc](https://www.pygame.org/docs/tut/PygameIntro.html)
  - Thirteen helpful tips: [pygame doc](https://www.pygame.org/docs/tut/newbieguide.html)
  - What to expect from pygame from the first principles: [Why pygame is slow](https://blubberquark.tumblr.com/post/630054903238262784/why-pygame-is-slow)

### Key takeaways

- What `pygame` is:
  - `pygame` is intented to be a *lightweight* *Pythonic* (yes, not just Python) *wrapper* for the *portable C SDL library*, which exposes API for multimedia accesses.
  - `pygame` was taken on by its author when a similar library `PySDL` is dead, which the author deems to be forcing a C-like style.
  - `pygame` performs software rendering (maybe by default). This means the CPU does the rendering, which prevents the CPU from performing other works.

- What `pygame` really is and is not:
  - `pygame` is intended to be a very simple, unopinionated library - it's not a game engine.
  - `pygame` can really run fast enough, based on your game. If writtent correctly, most of the time spent should be in the SDL C library. Although, some problems are inherent limited by the Python runtime, such as the GIL.

- Tips:
  - Make use of `Surface` & `Rect`. They are efficient & have diverse library functions in the library.
  - Should pre-convert images - `Surface.convert`.
  - Alphakey-blitting & per-pixel alpha are not the same thing.

## Design

- Choices:
  - Only abstract out necessary components, in this case, sprites - [`Animatable` sprites](/src/sprites/Animatable.py) and [`Static` sprites](/src/sprites/Static.py).
  - Other than the highly reusuable sprite-related classes, most other components are built up in an ad-hoc fashion for faster shipping & flexibility & receptive to changes.

In the next subsections, the highly abstracted sprites-related classes are documented.

### Sprite map

- A `SpriteMap` is simply a list of `pygame.Surface`, which is a preloaded list of images.
- An index into the `SpriteMap` represents an image to be rendered. Any sprites wanting to render an image will use these indexes.
- Pros: Memory savings.

### Animatable sprites

Most effort are spent abstracting out animations:
- `Animation`: A sequence of images, which internally is a sequence of indexes into `SpriteMap`.
- `AnimationSet`: A sequence of animations.
  - Motivation: A game object's state may require it to undergo different animations. For example, a *zombie* with the state *spawning* must undergo two animations (1) digging a hole and appearing (2) shifting left and right continuously.
  - Therefore, `AnimationSet` is a sequence of `Animation`s & also has a field called `fps` to control the speed of animation.
  - Pros: Allow reusing declared animations.
  - Cons: Currently not utilized (all `AnimationSet`s currently only contain one `Animation`).
- `Animatable`:
  - A base class for animatable game objects (i.e zombie, hammer).
  - A game object can switch between states. Each state should have an associated animation set. The methods on a game object that change its state should switch to the associated animation set.
  - Therefore, `Animatable` provides methods to allows switching between animation sets, setting positions, rendering the animation based on current time.

### Static sprites

A static game object is represented by the `Static` class, which allows setting its position & rendering based on current time.
