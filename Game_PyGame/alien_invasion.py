import sys
import pygame
from random import randint
from time import sleep

from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stat import GameStats

class AlienInvasion(): 
    """Класс для управления ресурсами и поведения игры"""

    def __init__(self):
        """Инициализация игры"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    
    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.y = alien.rect.height / 2 + 2 * alien.rect.height * row_number
        alien.rect.x = alien.x

        self.aliens.add(alien)

    def _create_fleet(self):
        """Создание флота вторжения"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        ship_height = self.ship.rect.height
        
        available_space_y = self.settings.screen_height - alien_height - ship_height
        number_rows = available_space_y // (2 * alien_height)   

        for row_number in range(number_rows):
            number_alien_x = randint(2, 5)
            for alien_namber in range(number_alien_x):
                self._create_alien(alien_namber, row_number)

    def _check_fleet_edges(self):
        """Реагирует на столкновение пришельцев с краями экрана"""
        for alien in self.aliens.sprites():
            if alien._check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает флот вниз и меняет направление"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Обрабатывает столкновение пришельца с кораблем"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()
       
            sleep(0.4)
        else:
            self.stats.game_active = False

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom() 

    def _upgrade_screen(self):
        """Обновляет изображение на экране"""
        self.screen.blit(self.settings.bg_img, (0, 0))
        self.ship.blitme()     

        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 

        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        if event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_events(self):
        """Обрабатывает события нажатия кнопки"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   sys.exit()
            elif event.type == pygame.KEYDOWN:
               self._check_keydown(event)
            elif event.type == pygame.KEYUP:
               self._check_keyup(event)

    def _fire_bullet(self):
        """Создание нового снаряда"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _check_aliens_bottom(self):
        """Проверяет столкновение пришельца с нижней частью экрана"""
        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:

            if self.stats.game_active:
                self._check_events()
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._upgrade_screen()
            else:
                pygame.quit()
            


start = AlienInvasion()
start.run_game()