import pygame.font


class Button:
    def __init__(self, screen, msg, x, y, dx, dy, button_color=(0, 0, 0), text_color=(0, 0, 0)):
        self.screen = screen
        self.msg = msg
        self.x = x
        self.y = y
        self.width, self.height = dx, dy
        self.font = pygame.font.SysFont(None, int(self.height/1.25))
        self.text_color = text_color
        self.button_color = button_color
        self.prep_button()

    def prep_button(self):
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(self.image, self.button_color, (0, 0, self.width, self.height), 1)
        self.button_image = self.font.render(self.msg, True, self.text_color)
        self.button_rect = self.button_image.get_rect()
        self.button_rect.center = self.rect.center

    def showme(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.button_image, self.button_rect)
