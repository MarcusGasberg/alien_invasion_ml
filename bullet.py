import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets sprites fired from the ship"""
    def __init__(self, game):
        """Create a bullet from the GameSettings and set the correct position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = game.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.player_ship.rect.midtop

        self.y = float(self.rect.y)
    
    def update(self):
        """Updates the bullets position on the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet onto the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)