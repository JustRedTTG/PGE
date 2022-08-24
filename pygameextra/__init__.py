"""PYGAME EXTRA __INIT__"""

import os
import pygame
from pygameextra.image import *
from pygameextra.sheet_handlers import *
from pygameextra.sprite import *
from pygameextra.modified import *
from pygameextra import event

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


def init(display_init_size=None):
    pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
    pygame.init()
    if display_init_size:
        display.make(display_init_size, mode=display.DISPLAY_MODE_HIDDEN)
