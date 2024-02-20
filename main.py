import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(30)
    screen.fill((255, 255, 255))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
