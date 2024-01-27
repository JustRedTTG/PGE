"""PYGAME EXTRA Modifications script
This script manages all pygame modifications"""
from typing import Union, List

import pygame
from pygameextra.rect import Rect
from pygameextra.sorters import layer_sorter
from typing import Union, IO


class SurfaceException(Exception):
    pass


class Surface:
    surface: pygame.Surface
    size: tuple
    layer: int
    display_tag: False

    def __init__(self, size: tuple = (0, 0), layer: int = 0, surface: pygame.Surface = None):
        if surface:
            self.size = surface.get_size()
            self.surface = surface
            self.layer = layer
        else:
            self.size = size
            self.surface = pygame.Surface(size, pygame.SRCALPHA)
            self.layer = layer
        self.area = None  # Used by stamps function
        self.pos = None  # Used by stamps function
        self.frames = 1  # Used by sprite animation function, if used improperly

    def stamp(self, source: Union['Surface', pygame.Surface], position: tuple = (0, 0), area: tuple = None,
              special_flags: int = 0):
        if type(source) is pygame.Surface:
            self.surface.blit(source, position, area, special_flags)
        else:
            self.surface.blit(source.surface, position, area, special_flags)

    def stamps(self, sources: List[Union['Surface', pygame.Surface]], positions: List[tuple] = None,
               areas: List[tuple] = None, special_flags: int = 0):
        if not positions:
            positions = [(0, 0)] * len(sources)
        if not areas:
            areas = [None] * len(sources)
        for i in range(len(sources)):
            sources[i].pos = positions[i]
            sources[i].area = areas[i]
        sources.sort(key=layer_sorter)
        for source in sources:
            self.surface.blit(source.surface, source.area, special_flags)

    def bind(self, layer: int):
        if self.layer >= 0 and layer >= 0:
            self.layer = layer
        elif layer < 0:
            raise SurfaceException("Can't bind a surface to a display surface layer.")
        else:
            raise SurfaceException("Can't bind a display surface to a surface layer.")

    def resize(self, size: tuple):
        self.surface = pygame.transform.scale(self.surface, size)
        self.size = self.surface.get_size()

    def flip(self, flip_x: bool = False, flip_y: bool = False):
        self.surface = pygame.transform.flip(self.surface, flip_x, flip_y)

    def copy(self) -> 'Surface':
        return Surface(self.size, self.layer, self.surface.copy())

    def get_at(self, x_y: tuple) -> tuple:
        return self.surface.get_at(x_y)

    def set_at(self, x_y: tuple, color: tuple) -> None:
        return self.surface.set_at(x_y, color)

    def set_alpha(self, alpha: int, flags: int = 0) -> None:
        return self.surface.set_alpha(alpha, flags)

    @property
    def rect(self) -> pygame.Rect:
        return self.surface.get_rect()

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]


SurfaceFileType = Union[str, IO, Surface, pygame.Surface]


def transparent_surface(area: tuple, alpha: int):
    new_surface = Surface(area)
    new_surface.set_alpha(alpha)
    return new_surface


def get_surface_file(file: SurfaceFileType, layer: int = 0) -> Surface:
    try:
        return Surface(surface=pygame.image.load(file).convert_alpha(), layer=layer)
    except TypeError:
        pass
        if isinstance(file, Surface):
            return file
        elif isinstance(file, pygame.Surface):
            return Surface(surface=file, layer=layer)
        else:
            raise TypeError("Please make sure file is a path / surface / file-like object")
