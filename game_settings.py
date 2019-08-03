class GameSettings:
    """A class to store all settings for the Alien Invasion game"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            #Display settings
            self.screen_width = kwargs["screen_width"] if "screen_width" in kwargs else 1200
            self.screen_height = kwargs["screen_height"] if "screen_height" in kwargs else 800
            self.bg_color = kwargs["bg_color"] if "bg_color" in kwargs else (230, 230, 230)

            #Ship settings
            self.ship_speed = kwargs["ship_speed"] if "ship_speed" in kwargs else 1.5

            #Bullet settings
            self.bullet_speed = 1.0
            self.bullet_width = 3
            self.bullet_height = 15
            self.bullet_color = (60, 60, 60)
            self.bullets_allowed = 3