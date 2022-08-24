import pygame
import pygameextra.display as display
from pygameextra.modified import *

def full(color: tuple):
    display.display_reference.surface.fill(color)


def transparency(color: tuple, alpha=255):
    new = pygame.Surface(display.display_reference.size, pygame.SRCALPHA)
    new.fill(color)
    new.set_alpha(alpha)
    display.display_reference.stamp(new)


def interlace(color: tuple, skips=2):
    new = pygame.Surface(display.display_reference.size, pygame.SRCALPHA)
    x, y = 0, 0
    w, h = new.get_size()
    while x < w:
        while y < h:
            new.set_at((x, y), color)
            y += skips
        y = 0
        x += skips
    display.display_reference.stamp(new)
