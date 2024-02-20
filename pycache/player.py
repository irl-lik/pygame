import pygame
from .entity import Entity


class Player(Entity):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple = None, image=None):
        super().__init__(x, y, width, height, color, image)

        self.name = "Вы"
        self.isJumping = False
        self.isFalling = False
        self.jumpCounter = 0
        self.speed_x = 0

    def draw(self, screen):
        return super().draw(screen)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.speed_x = max(self.speed_x - 2, -8)
        elif keys[pygame.K_d]:
            self.speed_x = min(self.speed_x + 2, 8)
        
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            if self.speed_x > 0:
                self.speed_x -= 2
            elif self.speed_x < 0:
                self.speed_x += 2

        self.x += self.speed_x

    def get_pos(self):
        return self.x, self.y