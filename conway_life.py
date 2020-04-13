# Programmed by Gocha Ugulava. GPL(v3)
# John Conway's Game of Life
#
# Memoriam of John Horton Conway (26 December 1937 – 11 April 2020)
#
# Sound from https://opengameart.org/
#  Some of the sounds in this project were created:
#              by Attribute Little Robot Sound Factory  www.littlerobotsoundfactory.com
#              by David McKee (ViRiX) www.soundcloud.com/virix


import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from sound import Sound
from button import Button


def main():
    game_set = Settings()
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))
    pygame.display.set_caption("Conway's Game of Life")
    gf.set_icon()
    sound = Sound(game_set)
    clock = pygame.time.Clock()

    button_start = Button(screen, "start", 80, 10, 160, 30)
    button_stop = Button(screen, "stop", 320, 10, 160, 30)
    button_clear = Button(screen, "clear", 560, 10, 160, 30)
    cells = Group()
    gf.create_cell(game_set, screen, cells)

    while True:
            clock.tick(game_set.fps)
            gf.check_event(game_set, cells, button_start, button_stop, button_clear, sound)
            if game_set.game_status == 'started':
                gf.step(game_set, cells, sound)
            gf.render(game_set, screen, cells, button_start, button_stop, button_clear)


if __name__ == "__main__":
    main()
