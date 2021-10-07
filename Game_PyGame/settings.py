import pygame

class Settings():
    """Класс для настроек игры"""

    def __init__(self):
        self.screen_width = 995
        self.screen_height = 690
        self.bg_img = pygame.image.load("images/background.png")
        self.bg_start = pygame.image.load("images/background_start.png")
        self.bg_inst = pygame.image.load("images/background_inst.png")
        self.icon = pygame.image.load("images/icon.png")

        self.ship_limit = 2

        self.bullet_width = 4
        self.bullet_height = 25
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 3
        
        self.fleet_drop_speed = 28

        self.speedup_scale = 1.05
        self.score_scale = 1.5
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        self.ship_speed = 3.0
        self.alien_speed = 1.8
        self.bullet_speed = 3.0

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


