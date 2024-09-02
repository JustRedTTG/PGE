import time
from typing import Tuple

import pygame

from pygameextra import settings, button, display, Rect
from pygameextra.mouse import pos, clicked


class Draggable:
    start_pos: tuple[int, int] = (0, 0)
    active: bool = False
    lock: bool = False
    scale_support: bool = False
    pos: tuple[int, int]
    area: [tuple[int, int], None]
    rect: pygame.Rect
    last_left_click: bool = False
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
        self.collide = False

    def _calculate(self):
        new_pos = self.pos
        current_pos = pos()
        difference = (current_pos[0] - self.start_pos[0], current_pos[1] - self.start_pos[1])
        return new_pos[0] + difference[0] * self.move_multiplier, new_pos[1] + difference[1] * self.move_multiplier

    def calculate(self) -> tuple:
        """calculate(self) -> tuple
        Gets the real time position of the draggable"""

        if not self.active:
            return self.pos
        return self._calculate()

    @property
    def button_name(self):
        return f"pygameextra.Draggable<{id(self)}>"

    def check(self) -> Tuple[bool, tuple]:
        """check(self) -> bool, tuple
        This function will check if the draggable is being moved and where it is"""

        if self.lock:
            return False, self.pos

        self.make_rect()
        if self.rect and not self.active:
            button.action(self.rect.copy(), hover_action=self.__setattr__, hover_data=('collide', True),
                          name=self.button_name)
            collide = self.collide and not settings.button_lock
        elif self.area is not None and self.active:
            button.action((*self._calculate(), *self.area), hover_action=self.__setattr__, hover_data=('collide', True),
                          name=self.button_name)
            collide = self.collide and not settings.button_lock
        else:
            button.action((0, 0, *display.get_size()), hover_action=self.__setattr__, hover_data=('collide', True),
                          name=self.button_name)
            collide = self.collide and not settings.button_lock
        if (collide and clicked()[0] and not self.last_left_click) and not self.active:
            self.active = True
            settings.button_lock = time.time()
            self.start_pos = pos()
        elif clicked()[0] and self.active:
            self.last_left_click = clicked()[0]
            return True, self._calculate()
        elif not clicked()[0] and self.active:
            self.active = False
            self.pos = self._calculate()

        self.last_left_click = clicked()[0]
        self.collide = False
        return False, self.pos
