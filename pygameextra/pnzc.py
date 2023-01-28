from typing import Callable
from pygameextra.mouse import Draggable, fingersupport
from pygameextra.math import lerp, dist

class PanAndZoomChunks:
    get_function: Callable
    visualization_function: Callable
    lazy_visualization_function: Callable
    movement_function: Callable
    pre_init_function: Callable
    lazy_pre_init_function: Callable

    zoom: int
    sizing: tuple[int, int]
    chunking_size: tuple[int, int]
    able: Draggable
    drag_speed: float
    drag_done: bool
    zooming: bool

    def __init__(
            self,
            get_function = lambda x, y, pnz: (x, y),
            visualization_function = lambda chunk, px, py, cx, cy, pnz: 0,
            lazy_visualization_function = lambda chunk, px, py, cx, cy, pnz: 0,
            movement_function = lambda old_x, old_y, new_x, new_y, pnz: 0,
            pre_init_function = lambda x, y, w, h, pnz: 0,
            mid_pre_init_function = lambda x, y, w, h, pnz: 0,
            lazy_pre_init_function = lambda x, y, w, h, pnz: 0,
            zoom: int = 1,
            size_per_chunk: tuple[int, int] = (50, 50),
            drag_speed: float = .01
        ):
        self.get_function = get_function
        self.visualization_function = visualization_function
        self.lazy_visualization_function = lazy_visualization_function
        self.movement_function = movement_function
        self.pre_init_function = pre_init_function
        self.lazy_pre_init_function = lazy_pre_init_function
        self.mid_pre_init_function = mid_pre_init_function

        self.zoom = zoom
        self.sizing = size_per_chunk
        self.chunking_size = size_per_chunk
        self.draggable = Draggable((0, 0), None)
        self.drag_smooth = self.draggable.pos
        self.drag_speed = drag_speed
        self.drag_done = True
        self.draggable.move_multiplier = 2
        self.zooming = False
    get_chunking_size = lambda self: self.chunking_size

    def event(self, x, y, w, h):
        moving, position = self.draggable.check()
        cs = self.get_chunking_size()
        if len(fingersupport.fingers) == 2:
            self.draggable.pos = position
            self.draggable.active = False
        if moving:
            self.lazy_pre_init_function(*self.drag_smooth, *cs, self)
            lazy = True
            self.drag_smooth = lerp(self.drag_smooth, position, self.drag_speed)
            self.drag_done = False
        elif not self.drag_done:
            self.mid_pre_init_function(*self.drag_smooth, *cs, self)
            lazy = True
            self.drag_smooth = lerp(self.drag_smooth, position, self.drag_speed)
            if dist(position, self.drag_smooth) < 5: self.drag_done = True
        else:
            self.pre_init_function(*self.drag_smooth, *cs, self)
            lazy = False

        # LOGIC FOR CHUNKS
        ox, oy = [v % cs[i] - cs[i]*1.5 for i, v in enumerate(self.drag_smooth)]
        for px in range(x, w+cs[0], cs[0]):
            for py in range(y, h+cs[1], cs[1]):
                cx, cy = self.get_chunk_at((px, py), cs)
                chunk = self.get_function(cx, cy, self)
                if lazy:
                    self.lazy_visualization_function(chunk, px+ox, py+oy, *cs, self)
                else:
                    self.visualization_function(chunk, px+ox, py+oy, *cs, self)

    def get_chunk_at(self, pos, chunking_size):
        x, y = pos
        x -= self.drag_smooth[0]
        y -= self.drag_smooth[1]
        cx, cy = chunking_size
        return x // cx, y // cy
