import pygame
from pygame.rect import RectType

from pygameextra.text import Text
from pygameextra.modified import Surface
from pygameextra import settings, Rect, fill, display
from pygameextra.assets import ASSET_FONT


class InputBox:
    _area: RectType
    _surface: Surface

    def __init__(self, area: RectType, font: [str, pygame.font.Font] = ASSET_FONT, initial_value: str = '', font_size: int = 20,
                 colors: [tuple, list] = ((255, 255, 255), None), antialias: bool = True):
        self.area = area
        self.value = [*initial_value]
        self.text = Text('', font, font_size, (0, 0), colors, antialias)
        self.refresh_text()
        self._surface = Surface(self.area.size)

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if isinstance(value, tuple):
            self._area = Rect(*value)
        else:
            self._area = value
        if getattr(self, '_surface', None):
            self._surface.resize(self.area.size)

    def refresh_text(self):
        self.text.text = ''.join(self.value)
        self.text.init()

        # Adjust text position
        self.text.rect.midright = self.area.midright
        self.text.rect.right -= self.text.font.get_height() * .4

        # Contextualize text position
        self.text.rect.top -= self.area.top
        self.text.rect.left -= self.area.left

    def display(self):
        settings.game_context.input_box_manager.input_boxes.append(self)
        with self._surface:
            fill.full((0, 0, 0, 0))
            self.text.display()

        display.blit(self._surface, self.area.topleft)





class StandaloneInputBoxManager:
    def __init__(self):
        self.input_boxes = []
        self.previous_input_boxes = []
        self.active_input_box = None

    def update_input_boxes(self):
        if self.active_input_box and self.active_input_box not in self.input_boxes:
            self.active_input_box = None

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
