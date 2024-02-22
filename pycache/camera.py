import pygame

class Camera():
    def __init__(self, total_width, total_height, win_width, win_height):
        self.state = pygame.Rect(0, 0, total_width, total_height)
        self.win_width = win_width
        self.win_height = win_height

    
    def get_pos(self):
        return self.state.x, self.state.y
    
    def camera_func(self, target_rect, FACT_WIDTH, FACT_HEIGHT):
        target_x = target_rect.x
        target_y = target_rect.y
        camera_x = target_x - self.win_width // 2
        camera_y = target_y - self.win_height // 2

        camera_x = max(camera_x, 0)
        camera_x = min(camera_x, FACT_WIDTH - self.win_width)
        camera_y = max(camera_y, 0)
        camera_y = min(camera_y, FACT_HEIGHT - self.win_height)

        return pygame.Rect(camera_x, camera_y, FACT_WIDTH, FACT_HEIGHT)

    def update(self, target_rect, FACT_WIDTH, FACT_HEIGHT):
        self.state = self.camera_func(target_rect, FACT_WIDTH, FACT_HEIGHT)