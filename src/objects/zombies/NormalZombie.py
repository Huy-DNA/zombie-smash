import pygame
from constants import ZOMBIE_DIE_ANIMATION_IDXES, ZOMBIE_SPAWN_ANIMATION_IDXES
from sprites.Animatable import Animatable
from sprites.Animation import Animation, Direction
from sprites.AnimationSet import AnimationSet


SPAWN_ANIMATION = Animation(
    sprite_idxes=ZOMBIE_SPAWN_ANIMATION_IDXES,
    should_loop=False,
    direction=Direction.BOTTOM_CENTER,
)

DESPAWN_ANIMATION = Animation(
    sprite_idxes=ZOMBIE_SPAWN_ANIMATION_IDXES[::-1],
    should_loop=False,
    direction=Direction.BOTTOM_CENTER,
)

KILL_ANIMATION = Animation(
    sprite_idxes=ZOMBIE_DIE_ANIMATION_IDXES,
    should_loop=False,
    direction=Direction.BOTTOM_CENTER,
)


class NormalZombie(Animatable):
    SPAWN_ANIMATION_SET = AnimationSet(queue=[SPAWN_ANIMATION], fps=60)
    DESPAWN_ANIMATION_SET = AnimationSet(queue=[DESPAWN_ANIMATION], fps=60)
    KILL_ANIMATION_SET = AnimationSet(queue=[KILL_ANIMATION], fps=100)

    def __init__(self, *, base_pos: tuple[float, float] = (0, 0)):
        self.set_base_pos(base_pos[0], base_pos[1])

    def spawn(self, *, start_ms: float = 0):
        self.set_animation_set(
            NormalZombie.SPAWN_ANIMATION_SET,
            start_ms=start_ms or pygame.time.get_ticks(),
        )

    def despawn(self, *, start_ms: float = 0):
        self.set_animation_set(NormalZombie.DESPAWN_ANIMATION_SET, start_ms=start_ms or pygame.time.get_ticks())

    def kill(self, *, start_ms: float = 0):
        self.set_animation_set(NormalZombie.KILL_ANIMATION_SET, start_ms=start_ms or pygame.time.get_ticks())
