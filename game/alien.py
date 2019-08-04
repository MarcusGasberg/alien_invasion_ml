import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single Alien in the fleet"""
    def __init__(self, game):
        """Initializes an Alien and stores relevant information about itself and the game"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    def check_edges(self):
        """Checks the aliens position relative to the edge of the screen.
        Returns true if alien is at the edge of the screen"""
        screen_rectangle = self.screen.get_rect()
        return self.rect.right >= screen_rectangle.right or self.rect.left <= 0
            