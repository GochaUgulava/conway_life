import pygame

import game_functions as gf


class Sound:
    def __init__(self, game_set):
        self.game_set = game_set
        self.set_cell = pygame.mixer.Sound(gf.get_path('set_cell.wav'))
        self.clear = pygame.mixer.Sound(gf.get_path('clear.wav'))
        self.start = pygame.mixer.Sound(gf.get_path('start.wav'))
        self.end = pygame.mixer.Sound(gf.get_path('end.wav'))

    def play(self, voice):
        voice.set_volume(self.game_set.sound_volume)
        voice.play()
