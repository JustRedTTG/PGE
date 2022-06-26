import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygameextra.image import *
from pygameextra.modified import *
from pygameextra import event


def init():
    pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
    pygame.init()