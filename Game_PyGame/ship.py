import pygame

class Ship():
    """Класс для управления кораблем"""

    def __init__(self, start_game):
        self.screen = start_game.screen
        self.screen_rect = start_game.screen.get_rect()
        self.settings = start_game.settings

        self.moving_right = False
        self.moving_left = False

        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль с текущей позиции"""
        self.screen.blit(self.image, self.rect) 
    
    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed