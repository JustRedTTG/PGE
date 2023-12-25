import pygame
from pygameextra import display, recorder, settings
from pygameextra.modified import *

line_cache = {}
rect_cache = {}
circle_cache = {}
ellipse_cache = {}
polygon_cache = {}


def line(color: tuple, pos_a: tuple, pos_b: tuple, w: int = 0, display_work: Surface = None):
    if len(color) > 3 and color[3] != 255:
        key = hash((color, pos_a, pos_b, w))
        if key in line_cache:
            new_surface, area = line_cache[key]
        else:
            top_left = tuple(min(a, b) - w // 2 for a, b in zip(pos_a, pos_b))
            bottom_right = tuple(max(a, b) + w // 2 for a, b in zip(pos_a, pos_b))
            area = (*top_left, *tuple(b - a for a, b in zip(top_left, bottom_right)))
            new_surface = transparent_surface(area[2:4], color[3])
            line(color[0:3], tuple(v - b for v, b in zip(pos_a, top_left)),
                 tuple(v - b for v, b in zip(pos_b, top_left)), w, new_surface)
            line_cache[key] = (new_surface, area)
        display_work = display_work if display_work else display.display_reference
        display_work.stamp(new_surface, area[0:2])
        return
    pygame.draw.line(display_work.surface if display_work else display.display_reference.surface, color, pos_a, pos_b,
                     w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawLine(color, pos_a, pos_b, w))


def rect(color: tuple, area: tuple, w: int = 0, display_work: Surface = None, edge_rounding: int = -1,
         edge_rounding_topright: int = -1, edge_rounding_topleft: int = -1, edge_rounding_bottomright: int = -1,
         edge_rounding_bottomleft: int = -1) -> None:
    if len(color) > 3 and color[3] != 255:
        key = hash((color, tuple(area), w))
        if key in rect_cache:
            new_surface = rect_cache[key]
        else:
            new_surface = transparent_surface(area[2:4], color[3])
            rect(color[0:3], (0, 0, *area[2:4]), w, new_surface, edge_rounding,
                 edge_rounding_topright, edge_rounding_topleft, edge_rounding_bottomright, edge_rounding_bottomleft)
            rect_cache[key] = new_surface
        display_work = display_work if display_work else display.display_reference
        display_work.stamp(new_surface, area[0:2])
        return
    pygame.draw.rect(display_work.surface if display_work else display.display_reference.surface, color, area, w,
                     border_radius=edge_rounding,
                     border_top_left_radius=edge_rounding_topleft,
                     border_top_right_radius=edge_rounding_topright,
                     border_bottom_left_radius=edge_rounding_bottomleft,
                     border_bottom_right_radius=edge_rounding_bottomright
                     )
    if not settings.recording:
        return
    recorder.record(recorder.DrawRect(color, area, w))


def circle(color: tuple, pos: tuple, radius: int, w: int = 0, display_work: Surface = None) -> None:
    if len(color) > 3 and color[3] != 255:
        key = hash((color, radius, w))
        if key in circle_cache:
            new_surface = circle_cache[key]
        else:
            new_surface = transparent_surface((radius * 2, radius * 2), color[3])
            circle(color[0:3], (radius, radius), radius, w, new_surface)
            circle_cache[key] = new_surface
        display_work = display_work if display_work else display.display_reference
        display_work.stamp(new_surface, tuple(v - radius for v in pos))
        return
    pygame.draw.circle(display_work.surface if display_work else display.display_reference.surface, color, pos, radius,
                       w, )
    if not settings.recording:
        return
    recorder.record(recorder.DrawCircle(color, pos, radius, w))


def ellipse(color: tuple, area: tuple, w: int = 0, display_work: Surface = None) -> None:
    if len(color) > 3 and color[3] != 255:
        key = hash((color, tuple(area), w))
        if key in ellipse_cache:
            new_surface = ellipse_cache[key]
        else:
            new_surface = transparent_surface(area[2:4], color[3])
            ellipse(color[0:3], (0, 0, *area[2:4]), w, new_surface)
            ellipse_cache[key] = new_surface
        display_work = display_work if display_work else display.display_reference
        display_work.stamp(new_surface, area[0:2])
        return
    pygame.draw.ellipse(display_work.surface if display_work else display.display_reference.surface, color, area, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawEllipse(color, area, w))


def polygon(color: tuple, points: [tuple, list], w: int = 0, display_work: Surface = None):
    if len(color) > 3 and color[3] != 255:
        key = hash((color, points, w))
        if key in polygon_cache:
            new_surface, area = polygon_cache[key]
        else:
            top_left = min(points, key=lambda point: point[0])[0], min(points, key=lambda point: point[1])[1]
            bottom_right = max(points, key=lambda point: point[0])[0], max(points, key=lambda point: point[1])[1]
            area = (*top_left, *tuple(b - a for a, b in zip(top_left, bottom_right)))
            new_surface = transparent_surface(area[2:4], color[3])
            polygon(color[0:3], tuple(tuple(v - b for v, b in zip(point, top_left)) for point in points), w,
                    new_surface)
            polygon_cache[key] = (new_surface, area)
        display_work = display_work if display_work else display.display_reference
        display_work.stamp(new_surface, area[0:2])
        return

    pygame.draw.polygon(display_work.surface if display_work else display.display_reference.surface, color, points, w)
    if not settings.recording:
        return
    recorder.record(recorder.DrawPolygon(color, points, w))
