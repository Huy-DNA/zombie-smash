import pygame

SpriteMap = list[pygame.Surface]

def loadSpriteMap(imagePaths: list[str]) -> SpriteMap:
    return [pygame.image.load(path) for path in imagePaths]
