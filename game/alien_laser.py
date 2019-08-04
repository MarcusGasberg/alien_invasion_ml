import pygame
from pygame.sprite import Sprite

class AlienLaser(Sprite):
    """A class to manage lasers fired from the aliens"""
    def __init__(self, game, shooter):
        """Create a bullet from the GameSettings and set the correct position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = game.settings.laser_color

        self.rect = pygame.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
        self.rect.midtop = shooter.rect.midbottom
        self.y = float(self.rect.y)
    
    def update(self):
        """Updates the bullets position on the screen"""
        self.y += self.settings.laser_speed
        self.rect.y = self.y

    def draw(self):
        """Draws the bullet onto the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)