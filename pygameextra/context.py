"""PYGAME EXTRA Contexts script
This script provides contexts which can be used to improve complex scenes"""
import pygame.event

from pygameextra import colors
from pygameextra import floating_methods
from pygameextra import fill
from pygameextra import display
from pygameextra import event
from pygameextra import settings
from pygameextra import time
from pygameextra.modified import Surface
from pygameextra.display import context_wrap
from pygameextra.mouse import offset_wrap
from typing import Union, Tuple
from abc import abstractmethod, ABC


class AreaUndefined(Exception):
    pass


class AreaBased(Exception):
    pass


class Context(ABC):
    BACKGROUND: Tuple[int, int, int] = colors.black
    AREA: Union[None, Tuple[int, int], Tuple[int, int, int, int]] = None
    FLOAT: Tuple[int, int] = floating_methods.FLOAT_CENTER

    surface: Surface = None
    _position: Tuple[int, int]
    area_based: bool = False

    def __init__(self):
        self.surface = Surface(self.size)
        if self.area_based:
            self._position = self.FLOAT
        else:
            self.position = self.AREA[:-2]
        self.surface.pos = self.position

    @abstractmethod
    def loop(self):
        pass

    def pre_loop(self):
        if self.BACKGROUND:
            fill.full(self.BACKGROUND)

    def post_loop(self):
        pass

    def start_loop(self):
        if self.area_based:
            self.update_float()

    def end_loop(self):
        display.blit(self.surface, self.surface.pos)

    def _loop(self):
        self.pre_loop()
        self.loop()
        self.post_loop()

    @property
    def size(self):
        if self.surface:
            return self.surface.size
        if self.AREA is None:
            raise AreaUndefined("Contexts require an AREA to be defined")
        elif isinstance(self.AREA, tuple) and len(self.AREA) == 2 and all(isinstance(x, int) for x in self.AREA):
            self.area_based = True
            return self.AREA
        elif isinstance(self.AREA, tuple) and len(self.AREA) == 4 and all(isinstance(x, int) for x in self.AREA):
            return self.AREA[2:]
        else:
            raise ValueError("AREA needs to be (width, height) + FLOAT or (x, y, width, height)")

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key == "FLOAT":
            if self.area_based:
                self._position = self.FLOAT
            else:
                raise AreaBased("Can't change the float in a non area based context")

    @property
    def position(self):
        if self.area_based and self.surface.pos is not None:
            return self.surface.pos
        return self._position

    @position.setter
    def position(self, value):
        if self.area_based:
            raise AreaBased("Can't change position in a AREA based context, change FLOAT instead")
        self._position = value
        self.surface.pos = self._position

    def resize(self, new_size):
        if not self.area_based:
            self.AREA = (self.AREA[:2], *new_size)
        else:
            self.AREA = new_size
            self.update_float()
        self.surface.resize(self.size)

    def __call__(self):
        @context_wrap(self.surface)
        @offset_wrap(tuple(map(lambda v: -v, self.surface.pos or (0, 0))))
        def run():
            return self._loop()

        def actual():
            self.start_loop()
            run()
            self.end_loop()

        return actual()

    def update_float(self):
        if not self.area_based:
            raise AreaBased("Updating the float position is only available for area based contexts")
        float_position = [1 if f > 0 else -1 if f < 0 else 0 for f in self._position]
        multiplier_position = [f + (-1 if f > 0 else 1) if f != 0 else 0 for f in self._position]

        display_position = [s // 2 * (1, 2, 0)[f] + (s // 2 * m) for s, f, m in
                            zip(display.get_size(), float_position, multiplier_position)]
        subtraction = [s // 2 * (1, 2, 0)[f] + (s // 2 * m) for s, f, m in
                       zip(self.size, float_position, multiplier_position)]

        self.surface.pos = tuple((pos - sub for pos, sub in zip(display_position, subtraction)))


class GameContext(Context, ABC):
    TITLE: str = "Game context"
    MODE: int = display.DISPLAY_MODE_NORMAL
    FPS: int = None

    def __init__(self):
        display.make(self.size, self.TITLE, self.MODE)
        self.surface = display.display_reference
        self.AREA = (0, 0, *display.get_size())
        self.area_based = False
        self._position = (0, 0)
        self.clock = time.clock
        settings.game_context = self
        self.buttons = []
        self.previous_buttons = []
        self.current_fps = self.FPS or 0
        while True:
            self()

    def start_loop(self):
        super().start_loop()
        self.buttons, self.previous_buttons = [], self.buttons

    def end_loop(self):
        self.current_fps = self.clock.get_fps()
        display.update(self.FPS)
        self.buttons.reverse()
        for button in self.buttons:
            button.logic()
            if button.hovered:
                break
        self.buttons.reverse()

    def __call__(self):
        self.events()
        self.start_loop()
        self._loop()
        self.end_loop()

    def handle_event(self, e: pygame.event.Event):
        if event.quitCheck():
            self.quit_check()

    def events(self):
        for event.c in event.get():
            self.handle_event(event.c)

    def quit_check(self):
        event.Pquit()

    @property
    def size(self):
        if self.AREA is None:
            self.MODE = display.DISPLAY_MODE_FULLSCREEN
            return (0, 0)
        return super().size

    @property
    def delta_time(self):
        return 1 / max(1, self.current_fps)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key == 'TITLE':
            display.set_caption(value)
