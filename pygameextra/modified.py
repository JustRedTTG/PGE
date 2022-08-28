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

    def __init__(self, size=(0, 0), layer=0, surface: pygame.Surface = None):
        if surface:
            self.size = surface.get_size()
            self.surface = surface
            self.layer = layer
        else:
            self.size = size
            self.surface = pygame.Surface(size)
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

    def copy(self):
        return Surface(self.size, self.layer, self.surface.copy())