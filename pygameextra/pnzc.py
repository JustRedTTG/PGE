import math
from typing import Callable
from pygameextra.mouse import Draggable, fingersupport
from pygameextra.math import lerp, dist


class PanAndZoomChunks:
    get_function: Callable
    visualization_function: Callable
    lazy_visualization_function: Callable
    movement_function: Callable  # TODO: add movement function
    lazy_movement_function: Callable  # TODO: add lazy movement function
    zooming_function: Callable
    lazy_zooming_function: Callable
    pre_init_function: Callable
    lazy_pre_init_function: Callable

    sizing: tuple[int, int]
    chunking_size: tuple[int, int]
    able: Draggable
    enable_smooth_drag: bool
    smooth_speed: float
    drag_done: bool

    zooming: bool
    zoom: float
    zoom_min: float
    zoom_max: float
    zoom_seed: float
    zoom_position: tuple[int, int]
    zoom_offset: tuple[int, int]
    zoom_chunking_size: tuple[int, int]
    zoom_length: float
    zoom_start: float
    zoom_start_position: float

    def __init__(
            self,
            get_function=lambda x, y, pnz: (x, y),
            visualization_function=lambda chunk, px, py, cx, cy, pnz: 0,
            lazy_visualization_function=lambda chunk, px, py, cx, cy, pnz: 0,
            movement_function=lambda old_x, old_y, new_x, new_y, pnz: 0,  # TODO add lazy movement
            zooming_function=lambda old_w, old_h, old_scale, new_w, new_h, new_scale, pnz: 0,
            lazy_zooming_function=lambda old_w, old_h, old_scale, new_w, new_h, new_scale, pnz: 0,
            pre_init_function=lambda x, y, w, h, pnz: 0,
            mid_pre_init_function=lambda x, y, w, h, pnz: 0,
            lazy_pre_init_function=lambda x, y, w, h, pnz: 0,
            zoom: int = 1,
            size_per_chunk: tuple[int, int] = (50, 50),
            smooth_speed: float = .01,
            enable_smooth_drag: bool = True,
            zoom_speed: float = .01,
            zoom_min: float = .1,
            zoom_max: float = 4
    ):
        self.get_function = get_function
        self.visualization_function = visualization_function
        self.lazy_visualization_function = lazy_visualization_function
        self.movement_function = movement_function
        # self.lazy_movement_function = lazy_movement_function # TODO: uncomment when lazy movement added
        self.zooming_function = zooming_function
        self.lazy_zooming_function = lazy_zooming_function
        self.pre_init_function = pre_init_function
        self.lazy_pre_init_function = lazy_pre_init_function
        self.mid_pre_init_function = mid_pre_init_function

        self.zoom = zoom
        self.sizing = size_per_chunk
        self.chunking_size = size_per_chunk
        self.draggable = Draggable((0, 0), None)
        self.enable_smooth_drag = enable_smooth_drag
        self.drag_smooth = self.draggable.pos
        self.smooth_speed = smooth_speed
        self.drag_done = True
        self.draggable.move_multiplier = 2
        self.zooming = False
        self.zoom_min = zoom_min
        self.zoom_max = zoom_max
        self.zoom_speed = zoom_speed

    def get_chunking_size(self):
        return [int(v * self.zoom) for v in self.chunking_size]

    def event(self, x, y, w, h):
        moving, position = self.draggable.check()
        cs = self.get_chunking_size()
        # Handle zooming!!
        if len(fingersupport.fingers) == 2:
            position = self.drag_smooth
            self.draggable.active = False
            self.draggable.pos = position
            self.drag_done = True
            if not self.zooming:
                self.zooming = True
                self.zoom_position = lerp(*[finger['pos'] for finger in fingersupport.fingers], .5)
                self.zoom_length = dist(*[finger['pos'] for finger in fingersupport.fingers])
                self.zoom_start = self.zoom
                self.zoom_start_position = position
                self.zoom_offset = [zp - zo for zo, zp in zip(position, self.zoom_position)]
                self.zoom_chunking_size = self.get_chunking_size()
            else:
                new_zoom_length = dist(*[finger['pos'] for finger in fingersupport.fingers])
                self.zoom = self.zoom_start + (new_zoom_length - self.zoom_length) * self.zoom_speed
                self.zoom = min(self.zoom_max, max(self.zoom_min, self.zoom))
                self.draggable.pos = [
                    # TODO: Fix shaking
                    zsp + (zo // self.zoom_start) * (self.zoom_start - self.zoom)
                    for zo, zp, zsp in zip(self.zoom_offset, self.zoom_position, self.zoom_start_position)
                ]
                self.lazy_zooming_function(*self.zoom_chunking_size, self.zoom_start, *self.get_chunking_size(),
                                           self.zoom, self)
                self.drag_smooth = self.draggable.pos
                lazy = True
                moving = False
        elif self.zooming:
            self.zooming = False
            self.lazy_zooming_function(*self.zoom_chunking_size, self.zoom_start, *self.get_chunking_size(), self.zoom,
                                       self)
        if moving:
            self.lazy_pre_init_function(*self.drag_smooth, *cs, self)
            lazy = True
            if self.enable_smooth_drag:
                self.drag_smooth = lerp(self.drag_smooth, position, self.smooth_speed)
                self.drag_done = False
            else:
                self.drag_smooth = position
        elif not self.drag_done:
            self.mid_pre_init_function(*self.drag_smooth, *cs, self)
            lazy = True
            self.drag_smooth = lerp(self.drag_smooth, position, self.smooth_speed)
            if dist(position, self.drag_smooth) < 5: self.drag_done = True
        else:
            self.pre_init_function(*self.drag_smooth, *cs, self)
            lazy = False

        # LOGIC FOR CHUNKS
        ox, oy = [v % cs[i] - cs[i] * 1.5 for i, v in enumerate(self.drag_smooth)]
        for px in range(x, w + cs[0], cs[0]):
            for py in range(y, h + cs[1], cs[1]):
                cx, cy = self.get_chunk_at((px, py), cs)
                chunk = self.get_function(cx, cy, self)
                if lazy:
                    self.lazy_visualization_function(chunk, px + ox, py + oy, *cs, self)
                else:
                    self.visualization_function(chunk, px + ox, py + oy, *cs, self)

    def get_chunk_at(self, pos, chunking_size):
        x, y = pos
        x -= self.drag_smooth[0]
        y -= self.drag_smooth[1]
        cx, cy = chunking_size
        return x // cx, y // cy
