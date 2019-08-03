import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single Alien in the fleet"""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)