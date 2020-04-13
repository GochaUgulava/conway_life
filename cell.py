import pygame
from pygame.sprite import Sprite


class Cell(Sprite):
    def __init__(self, game_set, screen, x, y):
        super().__init__()
        self.game_set = game_set
        self.screen = screen
        self.alive = False
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.game_set.grid_size, self.game_set.grid_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = self.x * self.game_set.grid_size
        self.rect.y = 100 + self.y * self.game_set.grid_size
        pygame.draw.rect(self.image, self.game_set.grid_color,
                         (0, 0, self.game_set.grid_size, self.game_set.grid_size), 1)

    def update(self):
        self.alive = not self.alive
        if self.alive:
            circle_color = self.game_set.alive_cell_color
        else:
            circle_color = self.game_set.screen_background_color
        pygame.draw.circle(self.image, circle_color,
                           (self.game_set.grid_size//2, self.game_set.grid_size//2), (self.game_set.grid_size - 6) // 2)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
