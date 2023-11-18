"""PYGAME EXTRA Sprite script
This script manages all sprite functions"""
from typing import Union

import pygame
from pygameextra.rect import Rect
from pygameextra import display
from pygameextra import settings
from pygameextra.sheet import Sheet
from pygameextra.animator import Animator
from pygameextra.sheet_handlers import *


class Sprite:
    def __init__(self, sprite_reference: Union[Sheet, str, Animator], scale=None, pos: tuple = (0, 0), name="Sprite", pivot='topleft',
                 layer=0):
        if isinstance(sprite_reference, Sheet):  # Using sprite sheet
            self.reference = sprite_reference
            self.size = scale or (self.reference.handler.width, self.reference.handler.height)
        elif isinstance(sprite_reference, Animator):  # Using animator
            self.animator = sprite_reference
            self.reference = sprite_reference
            self.size = scale or (self.reference.width, self.reference.height)
        else:  # Using sprite image
            self.reference = Surface(surface=pygame.image.load(sprite_reference).convert_alpha(), layer=layer)
            if scale:
                self.reference.resize(scale)
            self.size = scale or self.reference.size
        self.pos = pos
        self.name = name
        self.layer = layer
        self.pivot = pivot

        # Animation
        self.index = 0
        self.speed = 0
        self.pong = False
        self.flip = False
        self.multiplier = 1

    def skip_frame(self, speed: int = None):
        """Skips to the next frame in the sprite animation, according to a speed variable"""
        self.index += speed or self.speed * self.delta_time * self.multiplier  # Add to the index, according to a speed variable
        if self.multiplier > 0 and self.index >= self.reference.frames - 1:  # Check direction and index
            if self.pong:
                self.multiplier *= -1  # Flip the pong
            elif self.index > self.reference.frames - 1:
                self.index = 0  # Reset frame index
        elif self.multiplier < 0 and self.index <= 0:  # Check reverse direction and reverse index
            if self.pong:
                self.multiplier *= -1  # Flip the pong
            elif self.index <= 0:
                self.index = self.reference.frames  # Reset frame index
        self.index = min(self.reference.frames - 1, max(0, self.index))

    def display(self, position=None, area=None):
        rect = Rect(0, 0, *self.size)
        rect.__setattr__(self.pivot, position or self.pos)

        if isinstance(self.reference, Sheet):  # Check if the reference is a sprite sheet
            # self.reference.surface.layer = self.layer  # Update the layer, just in case
            s = Surface((self.reference.handler.width, self.reference.handler.height))
            s.stamp(self.reference.surface, (0, 0),
                    self.reference.get(self))  # Display to area, according to the sprite sheet handler
        elif isinstance(self.reference, Animator):
            s = Surface((self.reference.width, self.reference.height))
            s.stamp(self.reference.surface, (0, 0),
                    self.reference.get(self))
        else:
            display.blit(self.reference, position or self.pos, area)  # Display an image
        if isinstance(self.reference, Union[Sheet, Animator]):
            s.resize(self.size)
            s.flip(flip_x=self.flip)
            display.blit(s, rect.topleft)
            self.skip_frame()

    @property
    def delta_time(self):
        if not settings.game_context:
            return 1
        return settings.game_context.delta_time