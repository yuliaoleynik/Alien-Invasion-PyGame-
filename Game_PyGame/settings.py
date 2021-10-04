import pygame

class Settings():
    """Класс для настроек игры"""

    def __init__(self):
        self.screen_width = 995
        self.screen_height = 690
        self.bg_img = pygame.image.load("images/background.png")

        self.ship_speed = 3
        self.ship_limit = 2

        self.bullet_speed = 3
        self.bullet_width = 4
        self.bullet_height = 25
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 3

        self.alien_speed = 1.8
        self.fleet_drop_speed = 28
        self.fleet_direction = 1
