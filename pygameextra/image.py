"""PYGAME EXTRA Image script
This script manages all image functions"""

import pygame
from pygameextra.modified import Surface
from pygameextra import display


class Image:
    def __init__(self, file, size=None, position: tuple = (0, 0), layer=0):
        try:
            self.surface = Surface(surface=pygame.image.load(file).convert_alpha(), layer=layer)
        except TypeError:
            if isinstance(file, Surface):
                self.surface = file
            elif isinstance(file, pygame.Surface):
                self.surface = Surface(surface=file, layer=layer)
            else:
                raise ValueError("Please make sure file is a path / surface / file-like object")
        self.pos = position

        if size:
            self.surface.resize(size)
        self.size = self.surface.size

    def display(self, position=None, area=None):
        display.blit(self.surface, position or self.pos, area)

    def resize(self, size: tuple):
        self.surface.resize(size)
        self.size = self.surface.size

    def flip(self, flip_x: bool = False, flip_y: bool = False):
        self.surface.flip(flip_x, flip_y)

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    def copy(self) -> 'Image':
        new_surface = self.surface.copy()
        return Image(new_surface)


