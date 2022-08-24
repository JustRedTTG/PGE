"""PYGAME EXTRA __INIT__"""

import os
# noinspection PyUnresolvedReferences
from pygameextra.pygame import pygame
from pygameextra.image import *
from pygameextra.sheet_handlers import *
from pygameextra.sprite import *
from pygameextra.modified import *
from pygameextra.fill import *
from pygameextra import event


def init(display_init_size=None):
    pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
    pygame.init()
    if display_init_size:
        display.make(display_init_size, mode=display.DISPLAY_MODE_HIDDEN)
