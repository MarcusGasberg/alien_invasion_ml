import pygame
from alien import Alien
from bullet import Bullet

class GameFactory:
    def __init__(self, game):
        self.game = game
        self.aliens = pygame.sprite.Group()

    def create_fleet(self):
        """Creates a fleet of Alien 's"""
        alien = Alien(self.game)
        alien_width, alien_height = alien.rect.size
        horizontal_available_space = self.game.settings.screen_width - (2 * alien_width)
        horizontal_num_aliens = horizontal_available_space // (2 * alien_width)
        vertical_available_space = self.game.settings.screen_height - (3 * alien_height) - self.game.player_ship.rect.height
        vertical_num_aliens = vertical_available_space // (2 * alien_height)
        for row_number in range(vertical_num_aliens):
            for alien_number in range(horizontal_num_aliens):
                self._create_alien(alien_number, row_number)
        return self.aliens

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self.game)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def create_bullet(self):
        return Bullet(self.game)