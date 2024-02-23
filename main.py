import pygame
from pycache.enemy import Enemy
from pycache.player import Player
from pycache.levels.level1 import get_level, level_rect_list
from pycache.camera import Camera


pygame.init()

WIDTH, HEIGHT = 1400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Инициализация уровня и камеры
tiles_list = level_rect_list()
total_level_width = len(get_level().split('\n')[0]) * 40
total_level_height = len(get_level().split('\n')) * 40
camera = Camera(total_level_width, total_level_height, WIDTH, HEIGHT)

# Инициализация игрока и противника
player_x = WIDTH / 2
player_y = HEIGHT - 90
player_width = 50
player_height = 50
player = Player(player_x, player_y, player_width, player_height, (0, 255, 0))
enemy1 = Enemy(WIDTH - 100, player_y - 250, total_level_height - HEIGHT, 100, 50, 5, (255, 0, 0))
enemy2 = Enemy(40, player_y - 250, total_level_height - HEIGHT, 20, 20, 10, (121, 57, 81))
enemy1.set_name("E 1")
enemy2.set_name("E 2")

running = True
while running:
    clock.tick(40)
    screen.fill((0, 0, 0))

    # Отображение уровня

    # Обновление и отображение игрока и противника
    player.update()
    player_x, player_y = player.get_pos()
    # Обновление камеры
    camera.update(player.get_rect(), total_level_width, total_level_height)
    camera_x, camera_y = camera.get_pos()
    # Обновление врагов
    enemy1.move_towards_player(player_x, player_y, player_width, player_height, 500)
    enemy1.draw(screen, camera_x, camera_y)
    enemy2.move_towards_player(player_x, player_y, player_width, player_height, 500)
    enemy2.draw(screen, camera_x, camera_y)
    # Отрисовка игрока с учётом камеры
    player.draw(screen, camera_x, camera_y)
    # Применение сдвига камеры к всем объектам на уровне
    for tile in tiles_list:
        pygame.draw.rect(screen, (255, 58, 81), (tile.x - camera_x, tile.y - camera_y, tile.width, tile.height))

    # Обновление экрана
    pygame.display.update()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
