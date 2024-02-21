import pygame
from .entity import Entity
from .levels.level1 import level_rect_list


class Player(Entity):
    def __init__(self, x, y, width, height, color=None, image=None):
        super().__init__(x, y, width, height, color, image)

        self.name = "Вы"
        self.isJumping = False
        self.jumpCounter = 0
        self.speed_x = 0
        self.speed_y = 0
        self.tiles_list = level_rect_list()
        font = pygame.font.Font(None, 24)
        self.text_surface = font.render(self.name, True, (255, 255, 255))

    def set_name(self, name):
            self.name = name

    def draw(self, screen):
        super().draw(screen)
        if not self.name:
            return
        
        text_rect = self.text_surface.get_rect(center=(self.x + self.width // 2, self.y - 20))  # Получаем прямоугольник для позиционирования текста точно сверху Entrity
        screen.blit(self.text_surface, text_rect)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and keys[pygame.K_d]:
            if self.speed_x > 0:
                self.speed_x -= 2
            elif self.speed_x < 0:
                self.speed_x += 2
        elif keys[pygame.K_a]:
            self.speed_x = max(self.speed_x - 2, -8)
        elif keys[pygame.K_d]:
            self.speed_x = min(self.speed_x + 2, 8)
        
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            if self.speed_x > 0:
                self.speed_x -= 2
            elif self.speed_x < 0:
                self.speed_x += 2

        if keys[pygame.K_SPACE] and not self.isJumping:
            self.isJumping = True
            self.jumpCounter = 10
        if self.isJumping:
            self.speed_y = self.jumpCounter * 4 + 4
            print(self.speed_y)
            if self.jumpCounter != -10:
                self.jumpCounter -= 1

        self.speed_y -= 4

        player_rect = pygame.Rect(self.x + self.speed_x, self.y, self.width, self.height)
        for tile in self.tiles_list:
            if not player_rect.colliderect(tile): continue

            self.speed_x = 0

        player_rect = pygame.Rect(self.x, self.y - self.speed_y, self.width, self.height)
        for tile in self.tiles_list:
            if not player_rect.colliderect(tile): continue

            if self.speed_y > 0:
                self.speed_y = self.y - (tile.y + tile.height)
            elif self.speed_y < 0:
                self.speed_y = 0
                self.y = tile.y - self.height
                self.isJumping = False
            else:
                self.speed_y = 0
            self.jumpCounter = 0

        self.x += self.speed_x
        self.y -= self.speed_y

    def get_pos(self):
        return self.x, self.y