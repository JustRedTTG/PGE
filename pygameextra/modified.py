"""PYGAME EXTRA Modifications script
This script manages all pygame modifications"""

import pygame
from pygameextra.sorters import layer_sorter


class SurfaceException(Exception):
    pass


class Surface:
    surface = None
    size = None
    layer = 0
    display_tag = False

    def __init__(self, size=(0, 0), layer=0, surface: pygame.Surface = None):
        if surface:
            self.size = surface.get_size()
            self.surface = surface
            self.layer = layer
        else:
            self.size = size
            self.surface = pygame.Surface(size,pygame.SRCALPHA)
            self.layer = layer
        self.area = None  # Used by stamps function
        self.pos = None  # Used by stamps function
        self.frames = 1  # Used by sprite animation function, if used improperly

    def stamp(self, source: ['Surface', pygame.Surface], position=(0, 0), area=None, special_flags: int = 0):
        if type(source) == pygame.Surface:
            self.surface.blit(source, position, area, special_flags)
        else:
            self.surface.blit(source.surface, position, area, special_flags)

    def stamps(self, sources: list, positions: list = None, areas: list = None, special_flags: int = 0):
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

    def bind(self, layer):
        if self.layer >= 0 and layer >= 0:
            self.layer = layer
        elif layer < 0:
            raise SurfaceException("Can't bind a surface to a display surface layer.")
        else:
            raise SurfaceException("Can't bind a display surface to a surface layer.")

    def resize(self, size: tuple):
        self.surface = pygame.transform.scale(self.surface, size)
        self.size = self.surface.get_size()

    def copy(self) -> 'Surface':
        return Surface(self.size, self.layer, self.surface.copy())

    def get_at(self, x_y: tuple) -> tuple:
        return self.surface.get_at(x_y)

    def set_at(self, x_y: tuple, color: tuple) -> None:
        return self.surface.set_at(x_y, color)

    def set_alpha(self, alpha: int, flags: int = 0) -> None:
        return self.surface.set_alpha(alpha, flags)


def transparent_surface(area: tuple, alpha: int):
    new_surface = Surface(area)
    new_surface.set_alpha(alpha)
    return new_surface