import gc
import pygame
import sys
import ptObject

pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Polytronome")
FPS = 60
deltaTime = 0

clock = pygame.time.Clock()
running = True

sounds = (
    pygame.mixer.Sound("audio/accent_click.wav"),
    pygame.mixer.Sound("audio/click.wav"),
)


# Polytronome Objects
test = ptObject.PolytronomeObject(screen, sounds, 100, 5, (000, 200, 100), 4, 100)

test2 = ptObject.PolytronomeObject(
    screen, sounds, 100, 5, (200, 000, 100), 3, 100 * 3 / 4
)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((000, 000, 000))
    test.tick(deltaTime)
    test2.tick(deltaTime)
    test.draw()
    test2.draw()

    # Here the code may lay.

    pygame.display.flip()
    deltaTime = clock.tick(FPS) / 1000.0

gc.collect()
pygame.quit()
sys.exit()
