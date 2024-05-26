from pygameextra.modified import *


def full(color: tuple, display_work: Surface = None):
    display_work.surface.fill(color) if display_work else display.display_reference.surface.fill(color)


def transparency(color: tuple, alpha=255, display_work: Surface = None):
    new = pygame.Surface(display_work.size if display_work else display.display_reference.size, pygame.SRCALPHA)
    new.fill(color)
    new.set_alpha(alpha)
    # noinspection PyArgumentList
    display_work.stamp(new) if display_work else display.display_reference.stamp(new)


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
