import pygame
from pygameextra import display, recorder, settings
from pygameextra.modified import *


def line(color: tuple, pos_a: tuple, pos_b: tuple, w: int = 0, display_work: Surface = None):
    pygame.draw.line(display_work.surface if display_work else display.display_reference.surface, color, pos_a, pos_b, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawLine(color, pos_a, pos_b, w))


def rect(color: tuple, area: tuple, w: int = 0, display_work: Surface = None, edge_rounding: int = -1, edge_rounding_top_right: int = -1, edge_rounding_top_left: int = -1, edge_rounding_bottom_right: int = -1, edge_rounding_bottom_left: int = -1):
    pygame.draw.rect(display_work.surface if display_work else display.display_reference.surface, color, area, w,
                     border_radius=edge_rounding,
                     border_top_left_radius=edge_rounding_top_left,
                     border_top_right_radius=edge_rounding_top_right,
                     border_bottom_left_radius=edge_rounding_bottom_left,
                     border_bottom_right_radius=edge_rounding_bottom_right
                     )
    if not settings.recording:
        return
    recorder.record(recorder.DrawRect(color, area, w))


def circle(color: tuple, pos: tuple, radius: int, w: int = 0, display_work: Surface = None):
    pygame.draw.circle(display_work.surface if display_work else display.display_reference.surface, color, pos, radius, w, )
    if not settings.recording:
        return
    recorder.record(recorder.DrawCircle(color, pos, radius, w))


def ellipse(color: tuple, area: tuple, w: int = 0, display_work: Surface = None):
    pygame.draw.ellipse(display_work.surface if display_work else display.display_reference.surface, color, area, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawEllipse(color, area, w))

def polygon(color: tuple, points: [tuple, list], w: int = 0, display_work: Surface = None):
    pygame.draw.polygon(display_work.surface if display_work else display.display_reference.surface, color, points, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawPolygon(color, points, w))
