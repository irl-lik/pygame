import pygame

class Camera():
    def __init__(self, width, height):
        self.state = pygame.Rect(0, 0, width, height)

    
    def get_pos(self):
        return self.state.x, self.state.y
    
    def camera_func(self, target_rect, FACT_WIDTH, FACT_HEIGHT):
        l, t, _, _ = target_rect
        _, _, w, h = self.state
        l, t = -l + FACT_WIDTH / 2, -t + FACT_HEIGHT / 2

        l = min(0, l)                           # Не движемся дальше левой границы
        l = max(-(self.state.width - FACT_WIDTH), l)   # Не движемся дальше правой границы
        t = max(-(self.state.height - FACT_HEIGHT), t) # Не движемся дальше нижней границы
        t = min(0, t)                           # Не движемся дальше верхней границы

        return pygame.Rect(l, t, w, h)

    def update(self, target, FACT_WIDTH, FACT_HEIGHT):
        self.state = self.camera_func(target, FACT_WIDTH, FACT_HEIGHT)