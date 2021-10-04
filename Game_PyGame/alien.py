import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий одного пришельца"""

    def __init__(self, start_game):
        super().__init__()
        self.screen = start_game.screen
        self.settings = start_game.settings

        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):   
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        
    def _check_edges(self):
        """Возвращает True, если пришелец у края экрана"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
