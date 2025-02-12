from constants import HAMMER_IDX, HAMMER_SMASH_ANIMATION_IDXES
from sprites.Animatable import Animatable
from sprites.Animation import Animation, Direction
from sprites.AnimationSet import AnimationSet

BASE_ANIMATION = Animation(
    sprite_idxes=[HAMMER_IDX], should_loop=True, direction=Direction.CENTER_CENTER
)
SMASH_ANIMATION = Animation(
    sprite_idxes=HAMMER_SMASH_ANIMATION_IDXES,
    should_loop=False,
    direction=Direction.CENTER_CENTER,
)

class Hammer(Animatable):
    BASE_ANIMATION_SET = AnimationSet(queue=[BASE_ANIMATION], fps=60)
    SMASH_ANIMATION_SET = AnimationSet(queue=[SMASH_ANIMATION], fps=60)

    def __init__(self):
        self.set_animation_set(Hammer.BASE_ANIMATION_SET)

    def smash(self, *, start_ms: float = 0):
        self.set_animation_set(Hammer.SMASH_ANIMATION_SET, start_ms=start_ms)
