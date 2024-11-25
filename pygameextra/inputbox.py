import time
from typing import Union
import pygame
from pygame.rect import RectType

from pygameextra.text import Text
from pygameextra.modified import Surface
from pygameextra import button, mouse, settings, Rect, fill, display, draw, colors
from pygameextra.assets import ASSET_FONT


class InputBox:
    _area: RectType
    _padding: int
    _surface: Surface

    def __init__(self, area: RectType, font: Union[str, pygame.font.Font] = ASSET_FONT, initial_value: str = '', font_size: int = 20,
                 colors: Union[tuple, list] = ((255, 255, 255), None), antialias: bool = True):
        self.area = area
        self.value = [*initial_value]
        self.text_metrics = {}
        self.text = Text('', font, font_size, (0, 0), colors, antialias)
        self._padding = self.text.font.get_height() * .4
        self._left = self._padding
        self.refresh_text()
        self._surface = Surface(self.area.size)
        self._cursor_index = len(self.value)

    @property
    def area(self):
        return self._area
    
    @property
    def cursor_index(self):
        return self._cursor_index
    
    @cursor_index.setter
    def cursor_index(self, value):
        if self._cursor_index != value:
            self.input_box_manager.cursor_blink_timer = time.time()
        self._cursor_index = value
        

    @area.setter
    def area(self, value):
        if isinstance(value, tuple):
            self._area = Rect(*value)
        else:
            self._area = value
        if getattr(self, '_surface', None):
            self._surface.resize(self.area.size)

    def focus(self):
        self.input_box_manager.active_input_box = self

    def focus_to_cursor(self):
        if not mouse.clicked()[0]:
            return
        self.focus()
        with mouse.Offset(self.area.topleft, False, True):
            pos = mouse.pos()
        nearest_x = min(self.text_indexing, key=lambda x: abs(x - pos[0]))
        self.cursor_index = self.text_indexing.index(nearest_x)

    def refresh_text(self):
        self.text.text = ''.join(self.value)
        self.text.init()
        
        self.text_metrics = self.text.font.metrics(self.text.text)
        
        # Adjust text position
        self.text.rect.centery = self.area.height // 2
        self.text.rect.left = self._left

        # Calculate the x coordinates of each index
        self.text_indexing = []
        x = self.text.rect.left
        for metric in self.text_metrics:
            self.text_indexing.append(x)
            x += metric[4]
        self.text_indexing.append(x)

    @property
    def input_box_manager(self):
        return settings.game_context.input_box_manager

    @property
    def active(self):
        return self.input_box_manager.active_input_box == self
       
    @property
    def cursor_x(self):
        return self.text_indexing[self.cursor_index]

    def display(self):
        self.input_box_manager.input_boxes.append(self)
        with self._surface:
            fill.full((0, 0, 0, 0))
            self.text.display()
            # Enable click to focus and glide
            button.action((0, 0, *self.area.size), action=self.focus_to_cursor, hover_action=self.focus_to_cursor)
            if self.active:
                self.draw_cursor(self.input_box_manager.cursor_blink)
            
        
        display.blit(self._surface, self.area.topleft)

    def draw_cursor(self, active_blink: bool):
        if not active_blink:
            return
        draw.line(colors.white, (self.cursor_x, self.text.rect.top), (self.cursor_x, self.text.rect.bottom), 2)


class StandaloneInputBoxManager:
    CURSOR_BLINK_STAY = .3
    CURSOR_BLINK_DELAY = .4
    CURSOR_BLINK_TIMEOUT = CURSOR_BLINK_STAY + CURSOR_BLINK_DELAY
    def __init__(self):
        self.input_boxes = []
        self.previous_input_boxes = []
        self.active_input_box = None
        self.cursor_blink_timer = time.time()

    def update_input_boxes(self):
        if self.active_input_box and self.active_input_box not in self.input_boxes:
            self.active_input_box = None
        if self.active_input_box and mouse.clicked()[0] and not self.active_input_box.area.collidepoint(mouse.pos()):
            self.active_input_box = None
        if self.cursor_blink_timer + self.CURSOR_BLINK_TIMEOUT < time.time():
            self.cursor_blink_timer = time.time()
        
    @property
    def cursor_blink(self):
        return time.time() < self.cursor_blink_timer + self.CURSOR_BLINK_STAY

    def push_input_boxes(self):
        self.input_boxes, self.previous_input_boxes = [], self.input_boxes

    def handle_input_boxes(self, event):
        if not self.active_input_box:
            return


class ContextualizedInputBoxManager:
    def __init__(self, set_as_context: bool = True):
        self.input_box_manager = StandaloneInputBoxManager()
        if set_as_context:
            settings.game_context = self
