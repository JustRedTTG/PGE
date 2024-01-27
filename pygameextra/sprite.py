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


class Sprite:
    sheet_or_animator = False

    def __init__(self, sprite_reference: Union[Sheet, SurfaceFileType, Animator], scale=None, pos: tuple = (0, 0), name="Sprite",
                 pivot='topleft', layer=0, speed: float = 0):
        if isinstance(sprite_reference, Sheet):  # Using sprite sheet
            self.reference = sprite_reference
            self.size = scale or (self.reference.handler.width, self.reference.handler.height)
            self.sheet_or_animator = True
        elif isinstance(sprite_reference, Animator):  # Using animator
            self.animator = sprite_reference
            self.reference = sprite_reference
            self.size = scale or (self.reference.width, self.reference.height)
            self.sheet_or_animator = True
        elif isinstance(sprite_reference, SurfaceFileType):  # Using SurfaceFileType
            self.reference = get_surface_file(sprite_reference, layer)
            if scale:
                self.reference.resize(scale)
            self.size = scale or self.reference.size
        else:
            raise TypeError("Sprite reference should be of type Sheet | Animator or a Surface/File like object or path")
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
        if self.reference.loop:
            if self.multiplier > 0:
                self.index = 0
            elif self.multiplier < 0:
                self.index = self.reference.frames
        if isinstance(self.reference, Animator):
            self.reference.reset()

    def skip_frame(self, speed: int = None):
        """Skips to the next frame in the sprite animation, according to a speed variable"""
        if not isinstance(self.reference, Union[Animator, Sheet]):
            return
        self.index += speed or self.speed * self.delta_time * self.multiplier  # Add to the index, according to a speed variable
        if self.multiplier > 0 and self.index >= self.reference.frames - 1:  # Check direction and index
            if self.reference.pong:
                self.multiplier *= -1  # Flip the pong
            elif self.index > self.reference.frames - 1:
                self.reset()
        elif self.multiplier < 0 and self.index <= 0:  # Check reverse direction and reverse index
            if self.reference.pong:
                self.multiplier *= -1  # Flip the pong
            elif self.index <= 0:
                self.reset()
        self.index = min(self.reference.frames - 1, max(0, self.index))

    def display(self, position=None, area=None):
        rect = Rect(0, 0, *self.size)
        rect.__setattr__(self.pivot, position or self.pos)

        if isinstance(self.reference, Sheet):  # Check if the reference is a sprite sheet
            # self.reference.surface.layer = self.layer  # Update the layer, just in case
            s = Surface((self.reference.handler.width, self.reference.handler.height))
            if self.alpha:
                s.set_alpha(self.alpha, self.flags)
            s.stamp(self.reference.surface, (0, 0),
                    self.reference.get(self))  # Display to area, according to the sprite sheet handler
        elif isinstance(self.reference, Animator):
            s = Surface((self.reference.width, self.reference.height))
            if self.alpha:
                s.set_alpha(self.alpha, self.flags)
            s.stamp(self.reference.surface, (0, 0),
                    self.reference.get(self))
        else:
            display.blit(self.reference, position or self.pos, area)  # Display an image
        if self.sheet_or_animator:
            s.resize(self.size)
            s.flip(flip_x=self.flip_x, flip_y=self.flip_y)
            display.blit(s, rect.topleft)
            self.speed = self.reference.speed or self.speed or 0
            self.skip_frame()

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
        if isinstance(self.reference, Surface):
            return self.reference.set_alpha(alpha, flags)
        self.alpha = alpha
        self.flags = flags
