import pygame
from .entity import Entity
from .levels.level1 import level_rect_list

class Enemy(Entity):
    def __init__(self, x, y, absolute_y, width, height, speed, color=None, image=None):
        super().__init__(x, y, width, height, color, image)
        self.name = None
        self.speed = speed
        self.speed_x = 0
        self.speed_y = 0
        self.absolute_y = absolute_y
        self.isJumping = False
        self.isFalling = True
        self.jumpCounter = 0
        self.tiles_list = level_rect_list()

    def set_name(self, name):
        self.name = name
    
    def draw(self, screen, camera_x, camera_y):
        if self.image:
            screen.blit(self.image, (self.x - camera_x, self.y))
        elif self.color:
            pygame.draw.rect(screen, self.color, (self.x - camera_x, self.y - camera_y + self.absolute_y, self.width, self.height))
        if not self.name:
            return
        
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.name, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x - camera_x + self.width // 2, self.y - camera_y + self.absolute_y - 20))  # Получаем прямоугольник для позиционирования текста точно сверху Entrity
        screen.blit(text_surface, text_rect)
    
    def get_pos(self):
        return self.x, self.y
    
    def move_towards_player(self, player_x, player_y, player_width, player_height, distance_threshold=100):
        if self.is_player_nearby(player_x, player_y, distance_threshold):
            enemy_center_x = self.x + self.width / 2
            player_center_x = player_x + player_width / 2

            distance = player_center_x - enemy_center_x

            if distance < 0:
                self.speed_x = -min(self.speed, -distance)
            else:
                self.speed_x = +min(self.speed, distance)

        if self.isJumping and self.jumpCounter == 0 and not self.isFalling:
            self.jumpCounter = 10
        if self.isFalling:
            self.isJumping = False
        if self.isJumping:
            self.speed_y = self.jumpCounter * 4 + 4
            if self.jumpCounter != -10:
                self.jumpCounter -= 1

        enemy_rect = pygame.Rect(self.x + self.speed_x, self.y, self.width, self.height)
        for tile in self.tiles_list:
            if not enemy_rect.colliderect((tile.x, tile.y - self.absolute_y, tile.width, tile.height)): continue

            if self.speed_x > 0:
                self.speed_x = 0
                self.x = tile.x - self.width
            elif self.speed_x < 0:
                self.speed_x = 0
                self.x = tile.x + tile.width
            else:
                self.speed_x = 0
            self.isJumping = True
            self.jumpCounter = 0
            break

        self.speed_y -= 4

        
        self.isFalling = True
        enemy_rect = pygame.Rect(self.x, self.y - self.speed_y, self.width, self.height)
        for tile in self.tiles_list:
            if not enemy_rect.colliderect((tile.x, tile.y - self.absolute_y, tile.width, tile.height)): continue
            if self.speed_y > 0:
                self.speed_y = 0
                self.y = tile.y - self.absolute_y + tile.height
                self.isJumping = False
            elif self.speed_y < 0:
                self.speed_y = 0
                self.y = tile.y - self.absolute_y - self.height
            else:
                self.speed_y = 0
            self.jumpCounter = 0
            self.isFalling = False
            break

        self.y -= self.speed_y
        self.x += self.speed_x

    def camera_upd(self, camera_pos):
        self.x -= camera_pos[0]
        self.y -= camera_pos[1]

    def is_player_nearby(self, player_x, player_y, distance_threshold=100):
        distance = ((self.x - player_x)**2 + (self.y - player_y)**2) ** 0.5
        return distance < distance_threshold