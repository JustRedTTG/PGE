import time
import pygame
# noinspection PyUnresolvedReferences
from pygame.cursors import arrow, diamond, broken_x, tri_left, tri_right
from pygameextra.rect import Rect
from pygameextra import settings


def hide():
    pygame.mouse.set_visible(False)


def show():
    pygame.mouse.set_visible(True)


def icon(cursor_icon: pygame.cursors.Cursor = arrow):
    pygame.mouse.set_cursor(cursor_icon)


def pos(spoof: bool = True):
    if spoof and settings.enable_spoof:
        return settings.mouse_position or pygame.mouse.get_pos()
    return pygame.mouse.get_pos()


def clicked(spoof: bool = True):
    if spoof and settings.enable_spoof:
        return settings.mouse_clicked or pygame.mouse.get_pressed()
    return pygame.mouse.get_pressed()


class Draggable:
    start_pos = (0, 0)
    active = False
    pos = (0, 0)
    area = (0, 0)
    rect = None
    ltic = False

    def make_rect(self):
        if self.area:
            self.rect = Rect(*self.pos, *self.area)

    def __init__(self, position: tuple, area: tuple = None):
        self.pos = position
        self.area = area
        self.make_rect()

    def calculate(self):
        new_pos = self.pos
        current_pos = pos()
        difference = (current_pos[0] - self.start_pos[0], current_pos[1] - self.start_pos[1])
        return new_pos[0] + difference[0], new_pos[1] + difference[1]

    def check(self):
        self.make_rect()
        if self.rect:
            mouserect = Rect(*pos(), 1, 1)
            collide = self.rect.colliderect(mouserect) and not settings.button_lock
        else:
            collide = True
        if (collide and clicked()[0] and not self.ltic) and not self.active:
            self.active = True
            settings.button_lock = time.time()
            self.start_pos = pos()
        elif clicked()[0] and self.active:
            self.ltic = clicked()[0]
            return True, self.calculate()
        elif not clicked()[0] and self.active:
            self.active = False
            self.pos = self.calculate()
        self.ltic = clicked()[0]
        return False, self.pos
