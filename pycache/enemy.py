import pygame
from .entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, width, height, speed, color=None, image=None):
        super().__init__(x, y, width, height, color, image)
        self.name = None
        self.speed = speed
        self.x_speed = 0
        self.y_speed = 0

    def set_name(self, name):
        self.name = name
    

    def draw(self, screen):
        super().draw(screen)
        if not self.name:
            return
        
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.name, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y - 20))  # Получаем прямоугольник для позиционирования текста точно сверху Entrity
        screen.blit(text_surface, text_rect)
    
    def move_towards_player(self, player_x, player_y, player_width, player_height, distance_threshold=100):
        if self.is_player_nearby(player_x, player_y, distance_threshold):
            enemy_center_x = self.x + self.width / 2
            enemy_center_y = self.y + self.height / 2
            player_center_x = player_x + player_width / 2
            player_center_y = player_y + player_height / 2

            direction_x = player_center_x - enemy_center_x
            direction_y = player_center_y - enemy_center_y

            distance = (direction_x ** 2 + direction_y ** 2) ** 0.5
            if distance != 0:
                direction_x /= distance
                direction_y /= distance

            self.x_speed = direction_x * min(self.speed, distance)

            self.x += self.x_speed

        elif self.x_speed !=  0:
            self.x += self.x_speed
            if self.x_speed > 0:
                self.x_speed -= min(self.speed / 10, self.x_speed)
            else:
                self.x_speed += min(self.speed / 10, -self.x_speed)
    def is_player_nearby(self, player_x, player_y, distance_threshold=100):
        distance = ((self.x - player_x)**2 + (self.y - player_y)**2) ** 0.5
        return distance < distance_threshold