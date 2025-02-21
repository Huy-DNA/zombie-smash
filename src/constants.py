import os

from sprites.SpriteMap import loadSpriteMap

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

ASSETS_DIR = f"{os.getcwd()}/assets"

ICON_PATH = f"{ASSETS_DIR}/icon.png"

SPRITE_PATHS = (
    [f"{ASSETS_DIR}/normal-zombie/spawn/{img}.png" for img in range(1, 33)]
    + [f"{ASSETS_DIR}/background/tomb.png"]
    + [f"{ASSETS_DIR}/background/tomb_rocks.png"]
    + [f"{ASSETS_DIR}/background/grass.jpg"]
    + [f"{ASSETS_DIR}/hammer/base.png"]
    + [f"{ASSETS_DIR}/hammer/{img}.png" for img in range(1, 9)]
    + [f"{ASSETS_DIR}/normal-zombie/die/{img}.png" for img in range(1, 41)]
)
SPRITE_MAP = loadSpriteMap(SPRITE_PATHS)

ZOMBIE_SPAWN_ANIMATION_IDXES = list(range(32))
TOMB_IDX = 32
TOMB_ROCKS_IDX = 33
GRASS_IDX = 34
HAMMER_IDX = 35
HAMMER_SMASH_ANIMATION_IDXES = list(range(36, 44)) + list(range(43, 34, -1))
ZOMBIE_DIE_ANIMATION_IDXES = list(range(44, 84))
