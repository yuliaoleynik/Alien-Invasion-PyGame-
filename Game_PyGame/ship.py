import pygame

class Ship():
    """Класс для управления кораблем"""

    def __init__(self, start_game):
        self.screen = start_game.screen
        self.screen_rect = start_game.screen.get_rect()

        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль с текущей позиции"""
        self.screen.blit(self.image, self.rect) 