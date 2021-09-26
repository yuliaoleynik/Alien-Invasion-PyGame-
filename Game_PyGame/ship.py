import pygame

class Ship():
    """Класс для управления кораблем"""

    def __init__(self, start_game):
        self.screen = start_game.screen
        self.screen_rect = start_game.screen.get_rect()

        self.settings = start_game.settings

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.image_stand = pygame.image.load("images/ship.png")
        self.image_fly = pygame.image.load("images/ship2.png")

        self.rect = self.image_fly.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль с текущей позиции"""
        if self.moving_down or self.moving_up or self.moving_left or self.moving_right:
            self.screen.blit(self.image_fly, self.rect) 
        else: 
            self.screen.blit(self.image_stand, self.rect)  
    
    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed