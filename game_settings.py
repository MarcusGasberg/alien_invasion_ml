class GameSettings:
    """A class to store all settings for the Alien Invasion game"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            #Display settings
            self.screen_width = kwargs["screen_width"] if "screen_width" in kwargs else 1200
            self.screen_height = kwargs["screen_height"] if "screen_height" in kwargs else 800
            self.bg_color = kwargs["bg_color"] if "bg_color" in kwargs else (230, 230, 230)

        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        