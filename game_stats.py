import pygame

class GameStats:
    """Tracks the players stats for Alien Invasion"""

    def __init__(self, game):
        """Initialize Stats"""
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initailize/Reset stats for the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0