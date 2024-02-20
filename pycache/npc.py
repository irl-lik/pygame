from typing import Any
import pygame
from entity import *

class NPC(Entity):
    def __init__(self, x, y, width, height, color=None, image=None):
        super().__init__(x, y, width, height, color, image)
        self.name = None
        self.dialogue = None
    
    def set_name(self, name):
        self.name = name
    
    def set_dialogue(self, dialogue):
        self.dialogue = dialogue

    def draw(self, screen):
        super().draw(screen)
        if not self.name:
            return
        
        font = pygame.font.Font("arial", 24)
        text_surface = font.render(self.name, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y - 20))  # Получаем прямоугольник для позиционирования текста точно сверху Entrity
        screen.blit(text_surface, text_rect)
    
    def display_dialogue(self, screen, player_x, player_y):
        if not self.dialogue:
            return
        if not self.is_player_nearby(player_x, player_y):
            return

        font = pygame.font.Font("arial", 24)
        text_surface = font.render(self.dialogue, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y - 30 - text_surface.get_height()))
        screen.blit(text_surface, text_rect)
    
    def is_player_nearby(self, player_x, player_y, distance_threshold=100):
        distance = ((self.x - player_x)**2 + (self.y - player_y)**2) * 0.5
        return distance < distance_threshold