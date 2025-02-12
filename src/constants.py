import os

import pygame

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

BACKGROUND_MAIN_IMAGE = pygame.transform.scale(
    pygame.image.load(f"{ASSETS_DIR}/background/smashing-zombie-game.webp"),
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)
BACKGROUND_WIN_IMAGE = pygame.transform.scale(
    pygame.image.load(f"{ASSETS_DIR}/background/victory-scene.webp"),
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)
BACKGROUND_LOSE_IMAGE = pygame.transform.scale(
    pygame.image.load(f"{ASSETS_DIR}/background/loss.webp"),
    (SCREEN_WIDTH, SCREEN_HEIGHT),
)
LOGOUT_ICON = pygame.transform.scale(
    pygame.image.load(f"{ASSETS_DIR}/turn-off.png"), (30, 30)
)

# Sounds
# Base directory for sound files (assuming they are in a 'sounds' folder next to constants.py)
BASE_SOUND_DIR = os.path.join(ASSETS_DIR, "sounds")

# Define paths for each sound file
HIT_SOUND_PATH = os.path.join(BASE_SOUND_DIR, "hit.wav")
MISS_SOUND_PATH = os.path.join(BASE_SOUND_DIR, "miss.wav")
ZOMBIE_SPAWN_SOUND_PATH = os.path.join(BASE_SOUND_DIR, "zombie_spawn.wav")
ZOMBIE_DISAPPEAR_SOUND_PATH = os.path.join(BASE_SOUND_DIR, "zombie_disappear.flac")
BACKGROUND_SOUND_PATH = os.path.join(BASE_SOUND_DIR, "background.wav")
VICTORY_BACKGROUND_SOUND_PATH = os.path.join(BASE_SOUND_DIR, "victory_theme.wav")
LOSE_BACKGROUND_SOUND_PATH = os.path.join(BASE_SOUND_DIR, "lose_theme.wav")
