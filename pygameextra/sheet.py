"""PYGAME EXTRA Sheet script
This script manages the sheet class"""

import pygame
from pygameextra.modified import get_surface_file, SurfaceFileType
from pygameextra.sheet_handlers import *


class Sheet:
    def __init__(self, file: SurfaceFileType, handler: SheetHandler, speed: float = None, pong: bool = False,
                 loop: bool = False):
        self.surface = get_surface_file(file)
        handler.map(self.surface)
        self.handler = handler
        self.speed = speed
        self.pong = pong
        self.loop = loop
        self.frames = len(self.handler.mapping)

    def get(self, sprite: 'Sprite'):
        return self.handler.get(sprite)
