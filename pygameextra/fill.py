import pygameextra.display as display
import pygameextra.settings as settings
import pygameextra.recorder as recorder
from pygameextra.modified import *


def full(color: tuple, display_work: Surface = None):
    display_work.surface.fill(color) if display_work else display.display_reference.surface.fill(color)
    if not settings.recording and not display_work:
        return
    recorder.record(recorder.FillFull(color))


def transparency(color: tuple, alpha=255, display_work: Surface = None):
    new = pygame.Surface(display_work.size if display_work else display.display_reference.size, pygame.SRCALPHA)
    new.fill(color)
    new.set_alpha(alpha)
    # noinspection PyArgumentList
    display_work.stamp(new) if display_work else display.display_reference.stamp(new)
    if not settings.recording and not display_work:
        return
    recorder.record(recorder.FillTransparency(color, alpha))


def interlace(color: tuple, skips=2, display_work: Surface = None):
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
    display_work.stamp(new) if display_work else display.display_reference.stamp(new)
    if not settings.recording and not display_work:
        return
    recorder.record(recorder.FillInterlace(color, skips))
