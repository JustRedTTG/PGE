import pygame
from pygame.cursors import arrow, diamond, broken_x, tri_left, tri_right

def hide():
    pygame.mouse.set_visible(False)


def show():
    pygame.mouse.set_visible(True)


def icon(icon: pygame.cursors.Cursor = arrow):
    pygame.mouse.set_cursor(icon)


def pos():
    return pygame.mouse.get_pos()


def clicked():
    return pygame.mouse.get_pressed()


class Draggable:
    start_pos = (0, 0)
    active = False

    def __init__(self, position: tuple):
        self.pos = position

    def calculate(self):
        new_pos = self.pos
        current_pos = pos()
        difference = (current_pos[0] - self.start_pos[0], current_pos[1] - self.start_pos[1])
        return new_pos[0] + difference[0], new_pos[1] + difference[1]

    def check(self):
        if clicked()[0] and not self.active:
            self.active = True
            self.start_pos = pos()

        elif clicked()[0] and self.active:
            return True, self.calculate()
        elif not clicked()[0] and self.active:
            self.active = False
            self.pos = self.calculate()
        return False, self.pos
