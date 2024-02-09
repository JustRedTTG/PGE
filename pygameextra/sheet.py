"""PYGAME EXTRA Sheet script
This script manages the sheet class"""
from abc import abstractmethod

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
        self._frames = len(self.handler.mapping)

    @property
    def frames(self):
        return self._frames * (1 if not self.pong else 2)

    def get(self, sprite: 'Sprite'):
        return self.handler.get(sprite.index if not self.pong else (
            sprite.index if sprite.index < self._frames else self.frames - sprite.index
        ))

    @abstractmethod
    def custom_offset(self, rect, sprite: 'Sprite'):
        return rect
