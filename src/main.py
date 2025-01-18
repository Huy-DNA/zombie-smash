import pygame

from constants import SCREEN_SIZE

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

while True:
    # State update stage
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    screen.fill("black")
    # Render stage

    # Commit
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
