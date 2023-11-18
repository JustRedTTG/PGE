"""PYGAME EXTRA Sheet script
This script manages the sheet class"""

import pygame
from pygameextra.modified import Surface
from pygameextra.sheet_handlers import *


class Sheet:
    def __init__(self, file, handler: SheetHandler):
        self.surface = Surface(surface=pygame.image.load(file).convert_alpha())
        handler.map(self.surface)
        self.handler = handler
        self.frames = len(self.handler.mapping)

    def get(self, sprite: 'Sprite'):
        return self.handler.get(sprite)
