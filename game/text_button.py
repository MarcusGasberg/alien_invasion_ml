import pygame.font

class TextButton:
    """A Button containing a text message"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            self._game = kwargs["game"]
            self.screen = self._game.screen
            self.screen_rect = self.screen.get_rect()

            self.width, self.height = kwargs["size"] if "size" in kwargs else (200, 50)
            self.button_color = kwargs["button_color"] if "button_color" in kwargs else (0, 255, 0)
            self.text_color = kwargs["text_color"] if "text_color" in kwargs else (255, 255, 255)
            self.font = pygame.font.SysFont(None, 48)

            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center
            msg = kwargs["msg"] if "msg" in kwargs else ""
            self._render_msg(msg)
    
    def _render_msg(self, msg):
        """Turns a message into a rendered image and center text"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)