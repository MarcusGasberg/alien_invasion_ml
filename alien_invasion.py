import sys
import pygame
from game_settings import GameSettings
from space_ship import SpaceShip
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resourses"""
        pygame.init()
        self.settings = GameSettings(
            screen_height=800,
            screen_width=1200,
            bg_color=(230,230,230))
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.player_ship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start game loop"""
        while True:
            self._listen_for_event()
            self.player_ship.update()
            self._update_bullets()
            self._update_screen()
    
    def _listen_for_event(self):
        """Listens for game events like key presses etc"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._handle_key_down(event)
                elif event.type == pygame.KEYUP:
                    self._handle_key_up(event)

    def _handle_key_down(self, event):
        """Event handler for a key down event"""
        if event.key == pygame.K_RIGHT:
            self.player_ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player_ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_f:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
            self._fire_bullet()
    
    def _handle_key_up(self, event):
        """Event handler for a key up event"""
        if event.key == pygame.K_RIGHT:
            self.player_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player_ship.moving_left = False

    def _update_screen(self):
        """Updates the screen of the game"""
        self.screen.fill(self.settings.bg_color)
        self.player_ship.blit_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()
    
    def _update_bullets(self):
        """Updates the bullets on the screen. Removes them if not on screen"""
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        """Creates a new bullet for the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _create_fleet(self):
        """Creates a fleet of Alien 's"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        horizontal_available_space = self.settings.screen_width - (2 * alien_width)
        horizontal_num_aliens = horizontal_available_space // (2 * alien_width)
        vertical_available_space = self.settings.screen_height - (3 * alien_height) - self.player_ship.rect.height
        vertical_num_aliens = vertical_available_space // (2 * alien_height)
        for row_number in range(vertical_num_aliens):
            for alien_number in range(horizontal_num_aliens):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        alien.rect.x = alien.x
        self.aliens.add(alien)

if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()