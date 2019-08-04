import pygame

class GameStats:
    """Tracks the players stats for Alien Invasion"""

    def __init__(self, *args, **kwargs):
        """Initialize Stats"""
        self._game = kwargs["game"]
        self.settings = self._game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = kwargs["high_score"] if "high_score" in kwargs else 0

    def reset_stats(self):
        """Initailize/Reset stats for the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1