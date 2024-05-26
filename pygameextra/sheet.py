"""PYGAME EXTRA Sheet script
This script manages the sheet class"""
from abc import abstractmethod

import pygame
from pygameextra.modified import get_surface_file, SurfaceFileType
from pygameextra.sheet_handlers import *


class Sheet:
    def __init__(self, file: SurfaceFileType, handler: SheetHandler, speed: float = 0, pong: bool = False,
                 loop: bool = False, data: dict = None):
        self.surface = get_surface_file(file)
        handler.map(self.surface)
        self.handler: SheetHandler = handler
        self._speed = speed
        self.pong = pong
        self.loop = loop
        self.data = data if data is not None else {}

    @property
    def frames(self):
        return len(self.handler.mapping)

    @property
    def speed(self):
        return self._speed * (1 if not self.pong else .5)

    @speed.setter
    def speed(self, value):
        self._speed = value * (1 if not self.pong else 2)

    def get(self, sprite: 'Sprite'):
        if not self.pong:
            return self.handler.get(sprite.index)
        else:
            half = self.frames // 2
            if sprite.index < half:
                frame = sprite.index * 2
            else:
                frame = self.frames - (sprite.index - half) * 2
            return self.handler.get(frame) if sprite.multiplier > 0 else self.handler.get(self.frames - frame - 1)

    @staticmethod
    @abstractmethod
    def custom_offset(rect, sprite: 'Sprite', data: dict):
        return rect

    def handle_custom_offset(self, rect, sprite: 'Sprite'):
        return self.custom_offset(rect, sprite, self.data)
