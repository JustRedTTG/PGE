import time
from copy import copy
from functools import wraps
from typing import Tuple

import pygame
# noinspection PyUnresolvedReferences
from pygame.cursors import arrow, diamond, broken_x, tri_left, tri_right
from pygameextra import settings


def hide():
    pygame.mouse.set_visible(False)


def show():
    pygame.mouse.set_visible(True)


def icon(cursor_icon: pygame.cursors.Cursor = arrow):
    pygame.mouse.set_cursor(cursor_icon)


def pos(spoof: bool = True):
    position = settings.spoof_mouse_position \
        if settings.spoof_enabled and spoof and settings.spoof_mouse_position \
        else pygame.mouse.get_pos()
    if settings.spoof_enabled and spoof and settings.spoof_mouse_offset is not None:
        position = (position[0] + settings.spoof_mouse_offset[0],
                    position[1] + settings.spoof_mouse_offset[1])
    return position


def clicked(spoof: bool = True):
    if settings.spoof_enabled and spoof:
        return settings.spoof_mouse_clicked or pygame.mouse.get_pressed()
    return pygame.mouse.get_pressed()


def place(x, y):
    return pygame.mouse.set_pos([x, y])


def offset_wrap(offset: tuple, catch_error: bool = False, additive: bool = True, reverse: bool = False):
    def _offset_wrap(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            with Offset(offset, additive, reverse):
                if catch_error:
                    try:
                        result = func(*args, **kwargs)
                    except:
                        result = None
                else:
                    result = func(*args, **kwargs)
            return result

        return wrap

    return _offset_wrap


class Offset:
    def __init__(self, offset: tuple, additive: bool = True, reverse: bool = False):
        self.offset = offset
        self.additive = additive
        self.reverse = reverse

    def __enter__(self):
        self._backup = copy(settings.spoof_mouse_offset)
        if self.reverse:
            self.offset = map(lambda x: -x, self.offset)
        if self._backup is not None and self.additive:
            settings.spoof_mouse_offset = tuple(v + o for v, o in zip(self.offset, self._backup))
        else:
            settings.spoof_mouse_offset = tuple(self.offset)

    def __exit__(self, exc_type, exc_val, exc_tb):
        settings.spoof_mouse_offset = self._backup

    @classmethod
    def wrap(cls, offset: tuple, catch_error: bool = False, additive: bool = True, reverse: bool = False):
        return offset_wrap(offset, catch_error, additive, reverse)
