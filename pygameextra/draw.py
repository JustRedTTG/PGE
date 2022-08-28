import pygame
from pygameextra import display, recorder, settings


def line(color: tuple, pos_a: tuple, pos_b: tuple, w: int = 0):
    pygame.draw.line(display.display_reference.surface, color, pos_a, pos_b, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawLine(color, pos_a, pos_b, w))


def rect(color: tuple, area: tuple, w: int = 0):
    pygame.draw.rect(display.display_reference.surface, color, area, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawRect(color, area, w))


def circle(color: tuple, pos: tuple, radius: int, w: int = 0):
    pygame.draw.circle(display.display_reference.surface, color, pos, radius, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawCircle(color, pos, radius, w))


def ellipse(color: tuple, area: tuple, w: int = 0):
    pygame.draw.ellipse(display.display_reference.surface, color, area, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawEllipse(color, area, w))

def polygon(color: tuple, points: [tuple, list], w: int = 0):
    pygame.draw.polygon(display.display_reference.surface, color, points, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawPolygon(color, points, w))
