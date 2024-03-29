import pygame
from .entity import Entity
from .levels.level1 import level_rect_list


class Player(Entity):
    def __init__(self, x, y, width, height, speed, tiles_width, tiles_height, color=None, image=None):
        super().__init__(x, y, width, height, color, image)

        self.name = "Вы"
        self.isJumping = False
        self.isFalling = True
        self.jumpCounter = 0
        self.jumpWait = 0
        self.maxJumpWait = tiles_height // 2
        self.speed = speed
        self.speed_x = 0
        self.speed_y = 0
        self.tiles_list = level_rect_list(tiles_width, tiles_height)
        font = pygame.font.Font(None, 24)
        self.text_surface = font.render(self.name, True, (255, 255, 255))

    def set_name(self, name):
            self.name = name

    def draw(self, screen, camera_x, camera_y):
        if self.image:
            screen.blit(self.image, (self.x - camera_x, self.y - camera_y))
        elif self.color:
            pygame.draw.rect(screen, self.color, (self.x - camera_x, self.y - camera_y, self.width, self.height))
        
        if not self.name:
            return
        
        text_rect = self.text_surface.get_rect(center=(self.x - camera_x + self.width // 2, self.y - camera_y - 20))  # Получаем прямоугольник для позиционирования текста точно сверху Entrity
        screen.blit(self.text_surface, text_rect)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and keys[pygame.K_d]:
            if self.speed_x > 0:
                self.speed_x -= self.speed
            elif self.speed_x < 0:
                self.speed_x += self.speed
        elif keys[pygame.K_a]:
            self.speed_x = max(self.speed_x - self.speed, -self.speed * 4)
        elif keys[pygame.K_d]:
            self.speed_x = min(self.speed_x + self.speed, self.speed * 4)
        
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            if self.speed_x > 0:
                self.speed_x -= self.speed
            elif self.speed_x < 0:
                self.speed_x += self.speed

        if keys[pygame.K_SPACE] and not self.isJumping and self.jumpWait == 0 and not self.isFalling:
            self.isJumping = True
            self.jumpCounter = 10
            self.jumpWait = self.maxJumpWait
        if self.isJumping:
            self.speed_y = self.jumpCounter * 4 + 4
            if self.jumpCounter != -10:
                self.jumpCounter -= 1

        if self.jumpWait > 0: self.jumpWait -= 1

        self.speed_y -= 4

        player_rect = pygame.Rect(self.x + self.speed_x, self.y, self.width, self.height)
        for tile in self.tiles_list:
            if not player_rect.colliderect(tile): continue

            if self.speed_x > 0:
                self.speed_x = 0
                self.x = tile.x - self.width
            elif self.speed_x < 0:
                self.speed_x = 0
                self.x = tile.x + tile.width
            else:
                self.speed_x = 0
            break

        self.isFalling = True
        player_rect = pygame.Rect(self.x, self.y - self.speed_y, self.width, self.height)
        for tile in self.tiles_list:
            if not player_rect.colliderect(tile):
                continue

            if self.speed_y > 0:
                self.speed_y = 0
                self.y = tile.y + tile.height
            elif self.speed_y < 0:
                self.speed_y = 0
                self.y = tile.y - self.height
                self.isJumping = False
            else:
                self.speed_y = 0
            
            self.jumpCounter = 0
            self.isFalling = False
            break

        self.x += self.speed_x
        self.y -= self.speed_y

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def get_pos(self):
        return self.x, self.y