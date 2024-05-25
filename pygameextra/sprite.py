"""PYGAME EXTRA Sprite script
This script manages all sprite functions"""
from typing import Union

import pygame
from pygameextra.rect import Rect
from pygameextra import display, SurfaceFileType, get_surface_file
from pygameextra import settings
from pygameextra.sheet import Sheet
from pygameextra.animator import Animator
from pygameextra.sheet_handlers import *
from functools import lru_cache


class Sprite:
    sheet_or_animator = False
    reference: Union[Sheet, Surface, Animator]

    def __init__(self, sprite_reference: Union[Sheet, SurfaceFileType, Animator], resize: tuple = None,
                 scale: tuple = (1, 1), pos: tuple = (0, 0),
                 name="Sprite",
                 pivot='topleft', layer=0, speed: float = None):
        if isinstance(sprite_reference, Sheet):  # Using sprite sheet
            self.reference = sprite_reference
            self.resize = resize or (self.reference.handler.width, self.reference.handler.height)
            self.sheet_or_animator = True
        elif isinstance(sprite_reference, Animator):  # Using animator
            self.animator = sprite_reference
            self.reference = sprite_reference
            self.resize = resize
            self.sheet_or_animator = True
        elif isinstance(sprite_reference, SurfaceFileType):  # Using SurfaceFileType
            self.reference = get_surface_file(sprite_reference, layer)
            self.resize = resize or self.reference.size
        else:
            raise TypeError("Sprite reference should be of type Sheet | Animator or a Surface/File like object or path")
        self.scale = scale
        self.pos = pos
        self.name = name
        self.layer = layer
        self.pivot = pivot
        self.alpha = None
        self.flags = 0

        # Animation
        self.index = 0
        if self.sheet_or_animator:
            self.speed = self.reference.speed or speed or 0
        else:
            self.speed = speed or 0
        self.flip_x = False
        self.flip_y = False
        self.multiplier = 1

    def reset(self):
        reset_index = False
        if isinstance(self.reference, Animator):
            reset_index = self.reference.reset()

        if self.reference.loop or reset_index:
            if self.multiplier > 0:
                self.index = 0
            elif self.multiplier < 0:
                self.index = self.reference.frames

    def skip_frame(self, speed: int = None):
        """Skips to the next frame in the sprite animation, according to a speed variable"""
        if not isinstance(self.reference, Union[Animator, Sheet]):
            return
        self.index += speed or self.speed * self.delta_time * self.multiplier  # Add to the index, according to a speed variable
        if self.multiplier > 0 and self.index >= self.reference.frames - 1:  # Check direction and index
            self.reset()
        elif self.multiplier < 0 and self.index <= 0:  # Check reverse direction and reverse index
            self.reset()
        self.index = min(self.reference.frames - 1, max(0, self.index))

    @lru_cache(100)
    def _get_finished_surface(self, _1, _2, _3, _4, _5, _6, _7, _8, _9, _10):
        if isinstance(self.reference, Sheet):  # Check if the reference is a sprite sheet
            s = Surface((self.reference.handler.width, self.reference.handler.height))
            if self.alpha is not None:
                s.set_alpha(self.alpha, self.flags)
            s.stamp(self.reference.surface, (0, 0),
                    self.reference.get(self))  # Display to area, according to the sprite sheet handler
        elif isinstance(self.reference, Animator):
            s = Surface((self.reference.width, self.reference.height))
            if self.alpha is not None:
                s.set_alpha(self.alpha, self.flags)
            s.stamp(self.reference.surface, (0, 0),
                    self.reference.get(self))
        else:
            s = Surface(self.reference.size)
            if self.alpha is not None:
                s.set_alpha(self.alpha, self.flags)
            s.stamp(self.reference, (0, 0))
        s.resize(self.size)
        s.flip(flip_x=self.flip_x, flip_y=self.flip_y)
        return s

    def get_finished_surface(self):
        if self.sheet_or_animator:
            return self._get_finished_surface(
                self.speed, id(self.reference.surface), self.reference.get(self),
                (self.reference.handler.width, self.reference.handler.height) if isinstance(
                    self.reference, Sheet) else (self.reference.width, self.reference.height), self.flip_x, self.flip_y,
                self.size, self.alpha, self.flags, int(self.index)
            )
        else:
            return self._get_finished_surface(
                self.speed, id(self.reference.surface), None, self.reference.size, self.flip_x, self.flip_y,
                self.size, self.alpha, self.flags, None
            )

    def display(self, position=None, area=None):
        rect = Rect(0, 0, *self.size)
        rect.__setattr__(self.pivot, position or self.pos)

        if self.sheet_or_animator:
            s = self.get_finished_surface()
            display.blit(s, self.reference.handle_custom_offset(rect.copy(), self).topleft, area)
            self.speed = self.reference.speed or self.speed or 0
            self.skip_frame()
        else:
            display.blit(self.get_finished_surface(), position or self.pos, area)

    @property
    def delta_time(self):
        if not settings.game_context:
            return 1
        return settings.game_context.delta_time

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

    def set_alpha(self, alpha: int, flags: int = 0) -> None:
        self.alpha = alpha
        self.flags = flags

    @property
    def size(self):
        return tuple(
            resize * scale for resize, scale in zip(self.resize if self.resize else self.reference.size, self.scale))
