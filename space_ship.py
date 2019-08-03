import pygame

class SpaceShip:
    """A class to manage a space ship in the Alien Invasion game"""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rectangle = game.screen.get_rect()

        self.sprite = pygame.image.load("images/ship.bmp")
        self.rect = self.sprite.get_rect()
        self.rect.midbottom = self.screen_rectangle.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rectangle.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rectangle.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blit_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.sprite, self.rect)