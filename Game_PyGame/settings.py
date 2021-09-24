import pygame

class Settings():
    """Класс для настроек игры"""

    def __init__(self):
        self.screen_width = 995
        self.screen_height = 690
        self.bg_img = pygame.image.load("images/background.png")
