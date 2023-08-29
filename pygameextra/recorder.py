from pygameextra import settings, colors, display, draw, fill
from pygameextra.modified import Surface


def record(item):
    settings.recording_data.append(item)


class Blit:
    def __init__(self, obj, pos, area):
        self.obj = obj
        self.pos = pos
        self.area = area


class Button:
    def __init__(self, area, action, data):
        self.area = area
        self.action = action
        self.data = data


class FillFull:
    def __init__(self, color):
        self.color = color


class FillTransparency:
    def __init__(self, color, alpha):
        self.color = color
        self.alpha = alpha


class FillInterlace:
    def __init__(self, color, skips):
        self.color = color
        self.skips = skips


class DrawLine:
    def __init__(self, color, pos_a, pos_b, w):
        self.color = color
        self.pos_a = pos_a
        self.pos_b = pos_b
        self.w = w


class DrawRect:
    def __init__(self, color, area, w):
        self.color = color
        self.area = area
        self.w = w


class DrawCircle:
    def __init__(self, color, pos, radius, w):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.w = w


class DrawEllipse:
    def __init__(self, color, area, w):
        self.color = color
        self.area = area
        self.w = w


class DrawPolygon:
    def __init__(self, color, points, w):
        self.color = color
        self.points = points
        self.w = w


class Portion:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


def check_boundary(item):
    if type(item) == Blit:
        return *item.pos, *item.obj.get_size()
    elif type(item) == DrawLine:
        return (
            min(0, min(item.pos_a[0], item.pos_b[0])),
            min(0, min(item.pos_a[1], item.pos_b[1])),
            max(item.pos_a[0], item.pos_b[0]),
            max(item.pos_a[1], item.pos_b[1]),
        )
    elif (type(item) == DrawRect) or (type(item) == DrawEllipse):
        return item.area
    elif type(item) == DrawCircle:
        return (
            item.pos[0] - item.radius * .5,
            item.pos[1] - item.radius * .5,
            item.pos[0] + item.radius * .5,
            item.pos[1] + item.radius * .5,
        )
    elif type(item) == DrawPolygon:
        max_x = -100
        min_x = 100
        max_y = -100
        min_y = 100
        for point in item.points:
            max_x = max(max_x, point[0])
            min_x = min(min_x, point[0])
            max_y = max(max_y, point[1])
            min_y = min(min_y, point[1])
        return min_x, min_y, max_x - min_x, max_y - min_y
    return 0, 0, 1, 1


def sorter(item):
    if type(item) == display.display_reference.size:
        return 0
    return 1


def reconstruct(data: list):
    data.sort(key=sorter)
    rect = (0, 0, *data[0])
    size = data[0]
    del data[0]
    for item in data:
        boundary = check_boundary(item)
        rect = (
            min(boundary[0], rect[0]),
            min(boundary[1], rect[1]),
            max(boundary[0] + boundary[2], rect[2]),
            max(boundary[1] + boundary[3], rect[3]),
        )
    final_size = (rect[2] - rect[0], rect[3] - rect[1])
    offset = (-rect[0], -rect[1])
    surface = Surface(final_size)
    old_context = display.display_reference
    display.context(surface)

    for item in data:
        if type(item) == Blit:
            display.blit(item.obj, (item.pos[0] + offset[0], item.pos[1] + offset[1]), item.area)
        elif type(item) == FillFull:
            draw.rect(item.color, (*offset, *size))
        elif type(item) == FillTransparency:
            fill.transparency(item.color)
        elif type(item) == FillInterlace:
            fill.interlace(item.color)
        elif type(item) == DrawLine:
            draw.line(item.color, (item.pos_a[0] + offset[0], item.pos_a[1] + offset[1]),
                      (item.pos_b[0] + offset[0], item.pos_b[1] + offset[1]), item.w)
        elif type(item) == DrawRect:
            draw.rect(item.color, (item.area[0] + offset[0], item.area[1] + offset[1], item.area[2], item.area[3]),
                      item.w)
        elif type(item) == DrawEllipse:
            draw.ellipse(item.color, (item.area[0] + offset[0], item.area[1] + offset[1], item.area[2], item.area[3]),
                         item.w)
        elif type(item) == DrawCircle:
            draw.circle(item.color, (item.pos[0] + offset[0], item.pos[1] + offset[1]), item.radius, item.w)
        elif type(item) == DrawPolygon:
            points = []
            for point in item.points:
                points.append((point[0] + offset[0], point[1] + offset[1]))
            draw.polygon(item.color, points, item.w)

    draw.rect(colors.pge_dark, (*offset, *size), 2)
    draw.rect(colors.pge_light, (*offset, *size), 1)
    settings.recording_data.append(Portion(*offset, *size))

    # noinspection PyTypeChecker
    display.context(old_context)

    return surface


def comment(string: str = "Blank comment."):
    if settings.recording:
        settings.recording_data.append(string)


def padding_comment():
    comment('^========^')
