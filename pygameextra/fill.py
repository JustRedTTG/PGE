import pygameextra.display as display
import pygameextra.settings as settings
import pygameextra.recorder as recorder
from pygameextra.modified import *


def full(color: tuple):
    display.display_reference.surface.fill(color)
    if not settings.recording:
        return
    recorder.record(recorder.FillFull(color))


def transparency(color: tuple, alpha=255):
    new = pygame.Surface(display.display_reference.size, pygame.SRCALPHA)
    new.fill(color)
    new.set_alpha(alpha)
    # noinspection PyArgumentList
    display.display_reference.stamp(new)
    if not settings.recording:
        return
    recorder.record(recorder.FillTransparency(color, alpha))


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
    # noinspection PyArgumentList
    display.display_reference.stamp(new)
    if not settings.recording:
        return
    recorder.record(recorder.FillInterlace(color, skips))
