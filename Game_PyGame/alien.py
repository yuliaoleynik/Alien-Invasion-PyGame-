import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий одного пришельца"""

    def __init__(self, start_game):
        super().__init__()
        self.screen = start_game.screen

        self.image = pygame.image.load('images/alien2.png')
        self.rect = self.image.get_rect()

        