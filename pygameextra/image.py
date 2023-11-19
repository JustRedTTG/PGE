"""PYGAME EXTRA Image script
This script manages all image functions"""

import pygame
from pygameextra.modified import Surface
from pygameextra import display


class Image:
    def __init__(self, file, size=None, position: tuple = (0, 0), layer=0):
        self.surface = Surface(surface=pygame.image.load(file).convert_alpha(), layer=layer)
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
