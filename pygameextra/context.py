"""PYGAME EXTRA Contexts script
This script provides contexts which can be used to improve complex scenes"""

from pygameextra import colors
from pygameextra import floating_methods
from pygameextra import fill
from pygameextra import display
from pygameextra.modified import Surface
from pygameextra.display import context_wrap
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
        fill.full(self.BACKGROUND)

    def post_loop(self):
        pass

    def start_loop(self):
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
        self._position = value
        if self.area_based:
            raise AreaBased("Can't change position in a AREA based context, change FLOAT instead")
        self.surface.pos = self._position

    def __call__(self, *args, **kwargs):
        @context_wrap(self.surface)
        def run():
            return self._loop()

        def actual():
            self.start_loop()
            run()
            self.end_loop()

        return actual()

    def update_float(self):
        float_position = [1 if f > 0 else -1 if f < 0 else 0 for f in self._position]
        multiplier_position = [f+(-1 if f > 0 else 1) if f != 0 else 0 for f in self._position]

        display_position = [s//2 * (1, 2, 0)[f] + (s//2 * m) for s, f, m in zip(display.get_size(), float_position, multiplier_position)]
        subtraction = [s//2 * (1, 2, 0)[f] + (s//2 * m) for s, f, m in zip(self.size, float_position, multiplier_position)]

        self.surface.pos = tuple((pos - sub for pos, sub in zip(display_position, subtraction)))
