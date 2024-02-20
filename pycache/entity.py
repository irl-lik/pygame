import pygame

class Entity():
    def __init__(self, x, y, width, height, color=None, image=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color if color else None
        self.image = image if image else None
        if not self.image and not self.color:
            raise ValueError("Either image or color must be specified")
    
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        elif self.color:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))