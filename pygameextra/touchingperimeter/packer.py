from typing import Union, Tuple

from .func import *
from .box import Box
from pygameextra.rect import Rect


class Packer:
    def __init__(self, bin, rotating=False):
        self.bin = bin
        self.rotating = rotating
        self.packed = []
        self.free_rects = [bin]

    @classmethod
    def intersection(cls, rect1: Rect, rect2: Rect):
        if rect1.x >= rect2.right or rect1.right <= rect2.x or rect1.y >= rect2.bottom or rect1.bottom <= rect2.y:
            return None
        x = max(rect1.x, rect2.x)
        y = max(rect1.y, rect2.y)
        r = min(rect1.right, rect2.right)
        b = min(rect1.bottom, rect2.bottom)
        return Rect(x, y, r - x, b - y)

    @classmethod
    def substracted(cls, rect1: Rect, rect2: Rect):
        i = cls.intersection(rect1, rect2)
        if i is None:
            return [rect1.copy()]
        if i == rect1:
            return []
        tl = cls.inside(rect1, rect2.bottomleft)
        tr = cls.inside(rect1, rect2.bottomright)
        bl = cls.inside(rect1, rect2.topleft)
        br = cls.inside(rect1, rect2.topright)
        # check every case
        if tl and not (tr or bl or br):
            return [
                Rect(rect1.x, rect1.y, rect2.x - rect1.x, rect1.h),
                Rect(rect1.x, rect2.bottom, rect1.w, rect1.bottom - rect2.bottom)
            ]
        if tr and not (tl or bl or br):
            return [
                Rect(rect1.x, rect2.bottom, rect1.w, rect1.bottom - rect2.bottom),
                Rect(rect2.right, rect1.y, rect1.right - rect2.right, rect1.h)
            ]
        if bl and not (tl or tr or br):
            return [
                Rect(rect1.x, rect1.y, rect1.w, rect2.y - rect1.y),
                Rect(rect1.x, rect1.y, rect2.x - rect1.x, rect1.h)
            ]
        if br and not (tl or tr or bl):
            return [
                Rect(rect1.x, rect1.y, rect1.w, rect2.y - rect1.y),
                Rect(rect2.right, rect1.y, rect1.right - rect2.right, rect1.h)
            ]
        if tl and tr and not (bl or br):
            return [
                Rect(rect1.x, rect1.y, rect2.x - rect1.x, rect1.h),
                Rect(rect2.right, rect1.y, rect1.right - rect2.right, rect1.h),
                Rect(rect1.x, rect2.bottom, rect1.w, rect1.bottom - rect2.bottom)
            ]
        if tl and bl and not (tr or br):
            return [
                Rect(rect1.x, rect1.y, rect1.w, rect2.y - rect1.y),
                Rect(rect1.x, rect2.bottom, rect1.w, rect1.bottom - rect2.bottom),
                Rect(rect1.x, rect1.y, rect2.x - rect1.x, rect1.h)
            ]
        if tr and br and not (tl or bl):
            return [
                Rect(rect1.x, rect1.y, rect1.w, rect2.y - rect1.y),
                Rect(rect1.x, rect2.bottom, rect1.w, rect1.bottom - rect2.bottom),
                Rect(rect2.right, rect1.y, rect1.right - rect2.right, rect1.h)
            ]
        if bl and br and not (tl or tr):
            return [
                Rect(rect1.x, rect1.y, rect2.x - rect1.x, rect1.h),
                Rect(rect2.right, rect1.y, rect1.right - rect2.right, rect1.h),
                Rect(rect1.x, rect1.y, rect1.w, rect2.y - rect1.y)
            ]
        if tr and tl and bl and br:
            return [
                Rect(rect1.x, rect2.bottom, rect1.w, rect1.bottom - rect2.bottom),
                Rect(rect1.x, rect1.y, rect2.x - rect1.x, rect1.h),
                Rect(rect1.x, rect1.y, rect1.w, rect2.y - rect1.y),
                Rect(rect2.right, rect1.y, rect1.right - rect2.right, rect1.h)
            ]
        if (rect1.x < rect2.x < rect1.right) and (rect1.right <= rect2.right):
            return [
                Rect(rect1.x, rect1.y, rect2.x - rect1.x, rect1.h),
            ]
        if (rect1.y < rect2.y < rect1.bottom) and (rect1.bottom <= rect2.bottom):
            return [
                Rect(rect1.x, rect1.y, rect1.w, rect2.y - rect1.y),
            ]
        if (rect1.x < rect2.right < rect1.right) and (rect2.x <= rect1.x):
            return [
                Rect(rect2.right, rect1.y, rect1.right - rect2.right, rect1.h),
            ]
        if (rect1.y < rect2.bottom < rect1.bottom) and (rect2.y <= rect1.y):
            return [
                Rect(rect1.x, rect2.bottom, rect1.w, rect1.bottom - rect2.bottom),
            ]
        if rect1.x < rect2.x < rect1.right and rect1.x < rect2.right < rect1.right:
            return [
                Rect(rect1.x, rect1.y, rect2.x - rect1.x, rect1.h),
                Rect(rect2.right, rect1.y, rect1.right - rect2.right, rect1.h)
            ]
        if rect1.y < rect2.y < rect1.bottom and rect1.y < rect2.bottom < rect1.bottom:
            return [
                Rect(rect1.x, rect1.y, rect1.w, rect2.y - rect1.y),
                Rect(rect1.x, rect2.bottom, rect1.w, rect1.bottom - rect2.bottom)
            ]
        raise Exception('Should never get here! {} - {}'.format(rect1, rect2))

    @classmethod
    def inside(cls, rect1: Rect, rect2: Union[Rect, Tuple[int, int]]):
        if isinstance(rect2, Rect):
            return (rect2.x < rect1.x < rect2.right) and \
                (rect2.x < rect1.right < rect2.right) and \
                (rect2.y < rect1.y < rect2.bottom) and \
                (rect2.y < rect1.bottom < rect2.bottom)
        return (rect1.x < rect2[0] < rect1.right) and (rect1.y < rect2[1] < rect1.bottom)

    def pack(self, box):
        def get_free(b):
            def r_test(fr):
                return Rect(fr.x, fr.y, b.w, b.h)

            try:
                return max((touching_perimeter(self.packed + [self.bin], r_test(fr)), fr)
                           for fr in self.free_rects
                           if b.would_fit_in(fr) and \
                           touching_perimeter_left(self.packed + [self.bin], r_test(fr)) > 0 and \
                           touching_perimeter_bottom(self.packed + [self.bin], r_test(fr)) > 0)
            except ValueError:
                return None

        free_rect = get_free(box)
        if self.rotating:
            b_rotated = Box(box.h, box.w)
            free_rect_rotated = get_free(b_rotated)
            if not free_rect:
                free_rect = free_rect_rotated
                box = b_rotated
            elif free_rect_rotated and free_rect_rotated[0] > free_rect[0]:
                free_rect = free_rect_rotated
                box = b_rotated

        if free_rect is None:
            return False

        r = Rect(free_rect[1].x, free_rect[1].y, box.w, box.h)

        self.packed.append(r)

        self.free_rects = [fr for f in self.free_rects
                           for fr in self.substracted(f, r)
                           if (fr.width * fr.height) > 0
                           if touching_perimeter_left(self.packed + [self.bin], fr) > 0
                           if touching_perimeter_right(self.packed + [self.bin], fr) > 0
                           if touching_perimeter_top(self.packed + [self.bin], fr) > 0
                           if touching_perimeter_bottom(self.packed + [self.bin], fr) > 0]
        return True
