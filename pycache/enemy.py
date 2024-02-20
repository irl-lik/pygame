import pygame
from npc import NPC

class Enemy():
    def __init__(self, x, y, width, height, color=None, image=None):
        super().__init__(x, y, width, height, color, image)
        self.name = None

    def set_name(self, name):
        super().set_name(name)

    def draw(self, screen):
        super().draw(screen)

    def passing(self):
        pass

    def is_player_nearby(self, player_x, player_y, distance_threshold=100):
        super().is_player_nearby(player_x, player_y, distance_threshold)