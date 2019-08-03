class GameSettings:
    """A class to store all settings for the Alien Invasion game"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            #Display settings
            self.screen_width = kwargs["screen_width"] if kwargs["screen_width"] else 1200
            self.screen_height = kwargs["screen_height"] if kwargs["screen_height"] else 800
            self.bg_color = kwargs["bg_color"] if kwargs["bg_color"] else (230, 230, 230)

            #Ship settings
            self.ship_speed = kwargs["ship_speed"] if kwargs["ship_speed"] else 1.5
        