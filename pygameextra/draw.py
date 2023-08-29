import pygame
from pygameextra import display, recorder, settings
from pygameextra.modified import *


def line(color: tuple, pos_a: tuple, pos_b: tuple, w: int = 0, display_work: Surface = None):
    pygame.draw.line(display_work.surface if display_work else display.display_reference.surface, color, pos_a, pos_b,
                     w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawLine(color, pos_a, pos_b, w))


def rect(color: tuple, area: tuple, w: int = 0, display_work: Surface = None, edge_rounding: int = -1,
         edge_rounding_top_right: int = -1, edge_rounding_top_left: int = -1, edge_rounding_bottom_right: int = -1,
         edge_rounding_bottom_left: int = -1) -> None:
    if len(color) > 3:
        new_surface = transparent_surface((area[2], area[3]), color[3])
        rect((color[0], color[1], color[2]), (0, 0, area[2], area[3]), w, new_surface, edge_rounding,
             edge_rounding_top_right, edge_rounding_top_left, edge_rounding_bottom_right, edge_rounding_bottom_left)
        display_work = display_work if display_work else display.display_reference
        display_work.stamp(new_surface, (area[0], area[1]))
        return
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


def circle(color: tuple, pos: tuple, radius: int, w: int = 0, display_work: Surface = None) -> None:
    if len(color) > 3:
        new_surface = transparent_surface((radius * 2, radius * 2), color[3])
        circle((color[0], color[1], color[2]), (radius, radius), radius, w, new_surface)
        display_work = display_work if display_work else display.display_reference
        display_work.stamp(new_surface, (pos[0] - radius, pos[1] - radius))
        return
    pygame.draw.circle(display_work.surface if display_work else display.display_reference.surface, color, pos, radius,
                       w, )
    if not settings.recording:
        return
    recorder.record(recorder.DrawCircle(color, pos, radius, w))


def ellipse(color: tuple, area: tuple, w: int = 0, display_work: Surface = None) -> None:
    pygame.draw.ellipse(display_work.surface if display_work else display.display_reference.surface, color, area, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawEllipse(color, area, w))


def polygon(color: tuple, points: [tuple, list], w: int = 0, display_work: Surface = None):
    pygame.draw.polygon(display_work.surface if display_work else display.display_reference.surface, color, points, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawPolygon(color, points, w))
