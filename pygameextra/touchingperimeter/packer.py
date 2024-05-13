from .func import *
from .rect import Rect
from .box import Box

class Packer:
    def __init__(self, bin, rotating=False):
        self.bin = bin
        self.rotating = rotating
        self.packed = []
        self.free_rects = [bin]

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
            for fr in f.substracted(r)
            if fr.area() > 0
            if touching_perimeter_left(self.packed + [self.bin], fr) > 0
            if touching_perimeter_right(self.packed + [self.bin], fr) > 0
            if touching_perimeter_top(self.packed + [self.bin], fr) > 0
            if touching_perimeter_bottom(self.packed + [self.bin], fr) > 0]
        return True