import pygame
from pycache.enemy import Enemy
from pycache.player import Player
from pycache.levels.level1 import level_rect_list

pygame.init()

WIDTH, HEIGHT = 1400, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

running = True

player_x = WIDTH / 2
player_y = HEIGHT - 90

player_width = 50
player_height = 50

player = Player(player_x, player_y, player_width, player_height, (0, 255, 0))

enemy1 = Enemy(WIDTH, player_y, 100, 50, 5, (255, 0, 0))
enemy1.set_name("Enemy 1")
tiles_list = level_rect_list()

while running:
    clock.tick(30)
    screen.fill((0, 0, 0))

    for tile in tiles_list:
        pygame.draw.rect(screen, (255, 58, 81), tile)

    player.update()
    player_x, player_y = player.get_pos()

    enemy1.move_towards_player(player_x, player_y, player_width, player_height, 500)
    enemy1.draw(screen)
    player.draw(screen)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
