import sys
import pygame

from ship import Ship
from settings import Settings

class AlienInvasion(): 
    """Класс для управления ресурсами и поведения игры"""

    def __init__(self):
        """Инициализация игры"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   sys.exit()
            
            self.screen.blit(self.settings.bg_img, (0, 0))
            self.ship.blitme()
            
            pygame.display.flip()


start = AlienInvasion()
start.run_game()