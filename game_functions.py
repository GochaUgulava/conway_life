import os
import sys
import pygame
import copy
from time import sleep

from cell import Cell


class Point(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.rect = pygame.Rect(pos[0], pos[1], pos[0] + 1, pos[1] + 1)


def set_icon():
    icon_image = pygame.image.load(get_path("glider.ico"))
    pygame.display.set_icon(icon_image)


def get_path(file_name):
    game_folder = os.path.dirname(__file__)
    data_folder = os.path.join(game_folder, "data")
    file_path = os.path.join(data_folder, file_name)
    return file_path


def check_event(game_set, cells, button_start, button_stop, button_clear, sound):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            check_button(game_set, cells, button_start, button_stop, button_clear, pos, sound)


def check_button(game_set, cells, button_start, button_stop, button_clear, pos, sound):
    if button_start.rect.collidepoint(pos[0], pos[1]) and game_set.game_status == 'prepare':
        game_set.game_status = 'started'
        sound.play(sound.start)
    elif button_stop.rect.collidepoint(pos[0], pos[1]) and game_set.game_status == 'started':
        game_set.game_status = 'stopped'
        sound.play(sound.end)
    elif button_clear.rect.collidepoint(pos[0], pos[1]) and game_set.game_status != 'started':
        game_set.game_status = 'prepare'
        sound.play(sound.clear)
        clear(cells)
    elif pos[1] > 100 and game_set.game_status == 'prepare':
        check_button_field(cells, pos, sound)


def check_button_field(cells, pos, sound):
    mouse_sprite = Point(pos)
    collided_cell = pygame.sprite.spritecollideany(mouse_sprite, cells)
    if collided_cell:
        sound.play(sound.set_cell)
        collided_cell.update()


def create_cell(game_set, screen, cells):
    for x in range(0, 40):
        for y in range(0, 25):
            cell = Cell(game_set, screen, x, y)
            cells.add(cell)


def step(game_set, cells, sound):
    current_matrix = [[0] * 25 for i in range(40)]
    current_matrix_sum = 0
    # make current state matrix
    for cell in cells:
        current_matrix[cell.x][cell.y] = int(cell.alive)
        current_matrix_sum += int(cell.alive)
    # if current state matrix is empty call stop game function
    if current_matrix_sum == 0:
        game_set.game_status = 'stopped'
        sound.play(sound.end)
    # make new state matrix, analyzing each cell's neighbours
    new_matrix = copy.deepcopy(current_matrix)
    for x in range(0, 40):
        for y in range(0, 25):
            neighbour_sum = check_neighbour_sum(current_matrix, x, y)
            if neighbour_sum == 3 and current_matrix[x][y] == 0:
                new_matrix[x][y] = 1
            if (neighbour_sum < 2 or neighbour_sum > 3) and current_matrix[x][y] == 1:
                new_matrix[x][y] = 0
    # change board
    for cell in cells:
        if new_matrix[cell.x][cell.y] != current_matrix[cell.x][cell.y]:
            cell.update()
    sleep(0.5)


def check_neighbour_sum(current_matrix, x, y):
    neighbour_sum = 0
    for dx in (-1, 0, 1):
        if x + dx < 0 or x + dx > 39:
            continue
        for dy in (-1, 0, 1):
            if y + dy < 0 or y + dy > 24:
                continue
            if dx == 0 and dy == 0:
                continue
            neighbour_sum += current_matrix[x+dx][y+dy]
    return neighbour_sum


def clear(cells):
    for cell in cells:
        cell.alive = True
        cell.update()


def render(game_set, screen, cells, button_start, button_stop, button_clear):
    screen.fill(game_set.screen_background_color)
    button_start.showme()
    button_stop.showme()
    button_clear.showme()
    show_status(game_set, screen)
    cells.draw(screen)
    pygame.display.flip()


def show_status(game_set, screen):
    font = pygame.font.SysFont(None, 24)
    if game_set.game_status == 'prepare':
        msg = "status: prepare. set cells on board. press start button - to start game"
    elif game_set.game_status == 'started':
        msg = "status: started. press stop button to end the game"
    else:
        msg = "status: stopped. press clear button to prepare the board for new game"
    button_image = font.render(msg, True, game_set.grid_color)
    button_rect = button_image.get_rect()
    button_rect.center = (400, 75)
    screen.blit(button_image, button_rect)
