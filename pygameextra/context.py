"""PYGAME EXTRA Contexts script
This script provides contexts which can be used to improve complex scenes"""
from numbers import Number

import pygame.event

from pygameextra import colors
from pygameextra import floating_methods
from pygameextra import layer_methods
from pygameextra import fill
from pygameextra import display
from pygameextra import event
from pygameextra import settings
from pygameextra import time
from pygameextra.button import Button
from pygameextra.modified import Surface
from pygameextra.display import context_wrap
from pygameextra.mouse import offset_wrap
from pygameextra.fpslogger import Logger as FpsLogger
from typing import Union, Tuple
from abc import abstractmethod, ABC


class AreaUndefined(Exception):
    pass


class AreaBased(Exception):
    pass


class UnclippedContextException(Exception):
    pass


class Context(ABC):
    BACKGROUND: Tuple[Number, Number, Number] = colors.black
    AREA: Union[None, Tuple[Number, Number], Tuple[Number, Number, Number, Number]] = None
    FLOAT: Tuple[Number, Number] = floating_methods.FLOAT_CENTER

    surface: Surface = None
    _position: Tuple[Number, Number]
    area_based: bool = False
    pre_child_contexts: list
    post_child_contexts: list

    def __init__(self):
        self.surface = Surface(self.size)
        if self.area_based:
            self._position = self.FLOAT
        else:
            self.position = self.AREA[:-2]
        self.surface.pos = self.position
        self.pre_child_contexts = []
        self.post_child_contexts = []

    @abstractmethod
    def loop(self):
        pass

    def events(self):
        pass

    @staticmethod
    def handle_children(children):
        for child in children:
            child.parent_hooking()

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
        self.events()
        self.pre_loop()
        self.handle_children(self.pre_child_contexts)
        self.loop()
        self.handle_children(self.post_child_contexts)
        self.post_loop()
        self.pre_child_contexts = []
        self.post_child_contexts = []

    @property
    def size(self):
        if self.surface:
            return self.surface.size
        if self.AREA is None:
            raise AreaUndefined("Contexts require an AREA to be defined")
        elif isinstance(self.AREA, tuple) and len(self.AREA) == 2 and all(isinstance(x, Number) for x in self.AREA):
            self.area_based = True
            return self.AREA
        elif isinstance(self.AREA, tuple) and len(self.AREA) == 4 and all(isinstance(x, Number) for x in self.AREA):
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
        if self.surface:
            self.surface.pos = self._position

    def resize(self, new_size):
        if not self.area_based:
            self.AREA = (*self.position, *new_size)
        else:
            self.AREA = new_size
            self.update_float()
        if self.surface:
            self.surface.resize(new_size)

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


class ChildContext(ABC):
    LAYER = layer_methods.PRE_LAYER

    def __init__(self, parent: Context):
        self.parent_context = parent

    def pre_loop(self):
        pass

    def _loop(self):
        self.events()
        self.pre_loop()
        self.loop()
        self.post_loop()

    def post_loop(self):
        pass

    def parent_hooking(self):
        self._loop()

    def __call__(self):
        if self.LAYER == layer_methods.PRE_LAYER:
            self.parent_context.pre_child_contexts.append(self)
        elif self.LAYER == layer_methods.POST_LAYER:
            self.parent_context.post_child_contexts.append(self)

    def __getattr__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return self.parent_context.__getattribute__(item)
    def __setattr__(self, key, value):
        try:
            return super().__setattr__(key, value)
        except AttributeError:
            return self.parent_context.__setattr__(key, value)


class UnclippedContext(Context, ABC):
    FLOAT: Tuple[Number, Number] = floating_methods.FLOAT_TOPLEFT

    def __init__(self):
        print("UNCLIPPED CONTEXTS ARE DEPRECATED AS OF 2.0.0b41 USE THE NEW CHILD CONTEXT INSTEAD")
        self.surface = None
        self.area_based = True if self.AREA is None or len(self.AREA) == 2 else False
        if self.area_based:
            self._position = (0, 0)
        else:
            raise UnclippedContextException("Unclipped context cannot have a defined position")
        if self.FLOAT != floating_methods.FLOAT_TOPLEFT:
            raise UnclippedContextException("Float has to be topleft in an unclipped context")

    @property
    def size(self):
        if self.AREA is None:
            return display.get_size()
        return super().size

    def __call__(self):
        self.start_loop()
        self._loop()
        self.end_loop()

    def start_loop(self):
        pass

    def end_loop(self):
        pass


class GameContext(Context, ABC):
    TITLE: str = "Game context"
    MODE: int = display.DISPLAY_MODE_NORMAL
    FPS: int = None
    FPS_LOGGER: bool = False

    def __init__(self):
        display.make(self.size, self.TITLE, self.MODE)
        self.surface = display.display_reference
        self.AREA = (0, 0, *display.get_size())
        self.area_based = False
        self._position = (0, 0)
        self.clock = time.clock
        settings.game_context = self
        self.buttons: Button = []
        self.previous_buttons = []
        self.current_fps = self.FPS or 0
        self.fps_logger: FpsLogger = None
        if self.FPS_LOGGER:
            self._initialize_fps_logger()

    def _loop(self):
        self.events()
        self.pre_loop()
        self.loop()
        self.post_loop()

    def start_loop(self):
        super().start_loop()
        self.buttons, self.previous_buttons = [], self.buttons

    def end_loop(self):
        if self.FPS_LOGGER:
            self.fps_logger.render()
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

    def _initialize_fps_logger(self):
        self.fps_logger = FpsLogger()

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key == 'TITLE':
            display.set_caption(value)
        elif key == 'FPS_LOGGER':
            if value:
                if self.fps_logger is None:
                    self._initialize_fps_logger()
