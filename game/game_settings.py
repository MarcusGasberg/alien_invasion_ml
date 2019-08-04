class GameSettings:
    """A class to store all settings for the Alien Invasion game"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            #Display settings
            self.screen_width = kwargs["screen_width"] if "screen_width" in kwargs else 1200
            self.screen_height = kwargs["screen_height"] if "screen_height" in kwargs else 800
            self.bg_color = kwargs["bg_color"] if "bg_color" in kwargs else (230, 230, 230)

        #Ship settings
        self.ship_limit = 2

        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien laser settings
        self.laser_width = 3
        self.laser_height = 25
        self.laser_color = (255, 0, 0)
        self.lasers_allowed = 3
        
        #Scaling
        self.level_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.alien_points = 50
        self.fleet_direction = 1
        self.laser_speed = 1.2

    def increase_speed(self):
        """Increase speed settings using the level_scale"""
        self.ship_speed *= self.level_scale
        self.bullet_speed *= self.level_scale
        self.laser_speed *= self.level_scale
        self.alien_speed *= self.level_scale
        self.alien_points = int(self.alien_points * self.score_scale)