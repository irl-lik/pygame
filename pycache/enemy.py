import pygame
from .npc import NPC

class Enemy(NPC):
    def __init__(self, x: int, y: int, width: int, height: int, speed: int, color: tuple=None, image=None):
        super().__init__(x, y, width, height, color, image)
        self.name = None
        self.speed = speed
        self.x_speed = 0
        self.y_speed = 0

    def set_name(self, name: str):
        super().set_name(name)

    def draw(self, screen):
        super().draw(screen)
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
            self.y += direction_y * min(self.speed, distance)

        elif self.x_speed!= 0:
            self.x += self.x_speed
            if self.x_speed > 0:
                self.x_speed -= self.speed / 10
            else:
                self.x_speed += self.speed / 10
                print(self.x_speed)
    def is_player_nearby(self, player_x, player_y, distance_threshold=100):
        return super().is_player_nearby(player_x, player_y, distance_threshold)