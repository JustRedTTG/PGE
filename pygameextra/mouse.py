import time
import pygame
# noinspection PyUnresolvedReferences
from pygame.cursors import arrow, diamond, broken_x, tri_left, tri_right
from pygameextra.rect import Rect
from pygameextra import settings
from pygameextra import fingersupport


def hide():
    pygame.mouse.set_visible(False)


def show():
    pygame.mouse.set_visible(True)


def icon(cursor_icon: pygame.cursors.Cursor = arrow):
    pygame.mouse.set_cursor(cursor_icon)


def pos(spoof: bool = True):
    position = settings.spoof_mouse_position \
        if settings.spoof_enabled and spoof \
        else pygame.mouse.get_pos()
    if settings.spoof_enabled and settings.spoof_mouse_offset is not None and spoof:
        position = (position[0] + settings.spoof_mouse_offset[0],
                    position[1] + settings.spoof_mouse_offset[1])
    return position


def clicked(spoof: bool = True):
    if settings.spoof_enabled and spoof:
        return settings.spoof_mouse_clicked or pygame.mouse.get_pressed()
    return pygame.mouse.get_pressed()


def place(x, y):
    return pygame.mouse.set_pos([x, y])


class Draggable:
    start_pos: tuple[int, int]
    active: bool
    lock: bool
    scale_support: bool
    pos: tuple[int, int]
    area: [tuple[int, int], None]
    rect: pygame.Rect
    ltic: bool
    move_multiplier: float

    def make_rect(self):
        if self.area:
            self.rect = Rect(*self.pos, *self.area)

    def __init__(self, position: tuple[int, int], area: [tuple[int, int], None] = None,
                 move_multiplier: [float, int] = 1):
        self.pos = position
        self.area = area
        self.lock = False
        self.make_rect()
        self.rect = None
        self.active = False
        self.move_multiplier = move_multiplier

    def calculate(self):
        new_pos = self.pos
        current_pos = pos()
        difference = (current_pos[0] - self.start_pos[0], current_pos[1] - self.start_pos[1])
        return new_pos[0] + difference[0] * self.move_multiplier, new_pos[1] + difference[1] * self.move_multiplier

    def check(self):
        """check(self) -> bool, tuple
        This function will check if the draggable is being moved and where it is"""
        if self.lock:
            return False, self.pos

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
