from constants import HAMMER_IDX
from sprites.Animatable import Animatable
from sprites.Animation import Animation


class Hammer(Animatable):
    BASE_ANIMATION = Animation([HAMMER_IDX], True)

    def __init__(self):
        self.set_animation(Hammer.BASE_ANIMATION, 0)
        self.set_fps(60)
