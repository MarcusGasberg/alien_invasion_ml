import pygame.font

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, game):
        """Initialize scoreboard"""
        self._game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        score_str = "{:,}".format(round(self.stats.score, -1))
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = self.screen_rect.top

    def prep_high_score(self):
        high_score_str = "High score: {:,}".format(round(self.stats.high_score, -1))
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top


    def draw(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def update_high_score(self):
        """Updates the high score if the high score is beaten"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
