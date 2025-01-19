from constants import HAMMER_IDX, HAMMER_SMASH_ANIMATION_IDXES
from sprites.Animatable import Animatable
from sprites.Animation import Animation


class Hammer(Animatable):
    BASE_ANIMATION = Animation([HAMMER_IDX], True)
    SMASH_ANIMATION = Animation(HAMMER_SMASH_ANIMATION_IDXES, False)

    def __init__(self):
        self.set_animation(Hammer.BASE_ANIMATION, 0)
        self.set_fps(60)

    def smash(self, current_ms: float):
        self.set_animation(Hammer.SMASH_ANIMATION, current_ms)
        self.set_fps(60)
