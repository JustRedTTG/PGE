import string
import sys
import time
from typing import Union, Optional
import pygame
import pyperclip
from pygame.rect import RectType

from pygameextra.event import KeyHold, Key
from pygameextra.text import Text
from pygameextra.modified import Surface
from pygameextra import button, mouse, settings, Rect, fill, display, draw, colors, event
from pygameextra.assets import ASSET_FONT


class InputBox:
    _area: RectType
    _padding: int
    _surface: Surface
    DEFAULT_ALLOWED_CHARACTERS = (
        *string.ascii_letters,
        *string.digits,
        *string.punctuation,
        *string.whitespace,
    )

    def __init__(self, area: RectType, font: Union[str, pygame.font.Font] = ASSET_FONT, initial_value: str = '',
                 font_size: int = 20,
                 text_colors: Union[tuple, list] = (colors.black, None),
                 selected_colors=(colors.white, colors.aquamarine),
                 antialias: bool = True,
                 allowed_characters: tuple = DEFAULT_ALLOWED_CHARACTERS, return_action=None):
        self.return_action = return_action
        self.area = area
        self.value = initial_value
        self.text_metrics = {}
        self.text = Text('', font, font_size, (0, 0), text_colors, antialias)
        self.selected_text = Text('', font, font_size, (0, 0), selected_colors, antialias)
        self._padding = self.text.font.get_height() * .4
        self._left = self._padding
        self.text_indexing = []
        self.refresh_text()
        self._surface = Surface(self.area.size)
        self._cursor_index = len(self.value)
        self.allowed_characters = allowed_characters
        self._active_selection = None
        self._selection_hold = False

    @property
    def value(self):
        return ''.join(self._value)

    @value.setter
    def value(self, value: str):
        self._value = [*value]
        self.check_value()

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
        if -self._left > (new_left := (self.cursor_x_real - self._padding)):
            self._left = -new_left
        if -self._left + self.area.width < (new_right := self.cursor_x_real + self._padding):
            self._left = self.area.width - new_right
        self.position_text()

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

    def unfocus(self):
        self.input_box_manager.active_input_box = None

    @property
    def focused(self):
        return self.input_box_manager.active_input_box == self

    def focus_to_cursor(self):
        if not mouse.clicked()[0]:
            self._selection_hold = False
            return
        self.focus()
        with mouse.Offset(self.area.topleft, False, True):
            pos = mouse.pos()
        nearest_x = min(self.text_indexing, key=lambda x: abs(x - pos[0]))
        mods = pygame.key.get_mods()
        if mods & pygame.KMOD_SHIFT or self._selection_hold:
            self.select_to(self.text_indexing.index(nearest_x))
        elif not self._selection_hold:
            self.active_selection = None
        self._selection_hold = True
        self.cursor_index = self.text_indexing.index(nearest_x)

    def refresh_text(self):
        self.text.text = self.value
        self.text.init()

        self.text_metrics = self.text.font.metrics(self.text.text)

        self.position_text()

    def position_text(self):
        # Adjust text position
        self.text.rect.centery = self.area.height // 2
        self.text.rect.left = self._left

        # Calculate the x coordinates of each index
        self.text_indexing.clear()
        x = self.text.rect.left
        for metric in self.text_metrics:
            self.text_indexing.append(x)
            x += metric[4]
        self.text_indexing.append(x)

    def cut(self):
        left, right = self._pair_selection(*self.active_selection)
        del self._value[left:right]
        self.cursor_index = left
        self.refresh_text()
        self.active_selection = None

    def copy(self):
        if self.active_selection:
            left, right = self._pair_selection(*self.active_selection)
            return ''.join(self._value[left:right])
        return ''

    def backspace(self):
        if self.active_selection:
            self.cut()
            return
        if len(self.value) < 1 or self.cursor_index == 0:
            return
        del self._value[self.cursor_index - 1]
        self.cursor_index -= 1
        self.refresh_text()

    def delete(self):
        if self.active_selection:
            self.cut()
            return
        if (value_length := len(self.value)) < 1 or self.cursor_index == value_length:
            return
        del self._value[self.cursor_index]
        self.refresh_text()

    def right(self):
        if self.cursor_index < len(self.value):
            self.cursor_index += 1

    def left(self):
        if self.cursor_index > 0:
            self.cursor_index -= 1

    def action(self):
        if self.return_action:
            self.return_action()

    @property
    def input_box_manager(self):
        return settings.game_context.input_box_manager

    @property
    def active(self):
        return self.input_box_manager.active_input_box == self

    @property
    def cursor_x(self):
        return self.text_indexing[self.cursor_index]

    @property
    def cursor_x_real(self):
        return self.cursor_x - self._left

    def display(self):
        self.input_box_manager.input_boxes.append(self)
        with self._surface:
            fill.full((0, 0, 0, 0))
            self.text.rect.left = self._left
            self.text.display()
            if self.active_selection:
                self.draw_selection()
            # Enable click to focus and glide
            button.action(
                (0, 0, *self.area.size),
                action=self.focus_to_cursor,
                hover_action=self.focus_to_cursor,
                name=f'input_box_{id(self)}'
            )
            if self.active:
                self.draw_cursor(self.input_box_manager.cursor_blink)

        display.blit(self._surface, self.area.topleft)

    def draw_cursor(self, active_blink: bool):
        if not active_blink:
            return
        draw.line(self.text.color, (self.cursor_x, self.text.rect.top), (self.cursor_x, self.text.rect.bottom), 2)

    def draw_selection(self):
        draw.rect(self.selected_text.background, self.selected_text.rect.inflate(self._padding / 2, self._padding / 2),
                  1)
        self.selected_text.display()

    def check_value(self):
        pass

    @staticmethod
    def _pair_selection(*values):
        # Ensure the values are in ascending order
        left = min(values)
        right = max(values)
        return left, right

    @property
    def active_selection(self):
        return self._active_selection

    @active_selection.setter
    def active_selection(self, value):
        if value is None:
            self._active_selection = None
            self.selected_text.text = ''
            self.selected_text.init()
            return
        # Get the indexes in order from the selection
        left, right = self._pair_selection(*value)  # unpack the selection
        self._active_selection = value

        # Update the selected text
        self.selected_text.text = self.value[left:right]
        self.selected_text.init()

        # Update the selected text position to match the input box
        self.selected_text.rect.left = self.text_indexing[left]
        self.selected_text.rect.centery = self.text.rect.centery

    def select_to(self, index):
        if index < 0 or index > len(self.value):
            return
        if self.active_selection is None and self.cursor_index != index:  # Create a new selection
            self.active_selection = (self.cursor_index, index)
        elif self.active_selection:  # Update the existing selection from its origin
            self.active_selection = (self.active_selection[0], index)


# noinspection PyProtectedMember
class StandaloneInputBoxManager:
    CURSOR_BLINK_STAY = .3
    CURSOR_BLINK_DELAY = .4
    CURSOR_BLINK_TIMEOUT = CURSOR_BLINK_STAY + CURSOR_BLINK_DELAY

    def __init__(self):
        self.input_boxes = []
        self.previous_input_boxes = []
        self._active_input_box: Optional[InputBox] = None
        self.key_hold = KeyHold()
        self.cursor_blink_timer = time.time()

    @property
    def active_input_box(self):
        return self._active_input_box

    @active_input_box.setter
    def active_input_box(self, value):
        if value is None:
            self.key_hold.clear()
        self._active_input_box = value

    def update_input_boxes(self):
        if self.active_input_box and self.active_input_box not in self.input_boxes:
            self.active_input_box.unfocus()
        if self.active_input_box and any(mouse.clicked()) and not self.active_input_box.area.collidepoint(mouse.pos()):
            self.active_input_box.unfocus()
        if self.cursor_blink_timer + self.CURSOR_BLINK_TIMEOUT < time.time():
            self.cursor_blink_timer = time.time()
        if not self.active_input_box:
            return
        for key in self.key_hold.handle_hold():
            self.handle_key_action_hold(key)

    def handle_key_action_press(self, key: Key):
        if key == pygame.K_RETURN or key == pygame.KSCAN_RETURN:
            self.active_input_box.action()
        elif event.check_home(key):
            self.active_input_box.cursor_index = 0
        elif event.check_end(key):
            self.active_input_box.cursor_index = len(self.active_input_box.value)
        else:
            return False
        return True

    def handle_key_action_hold(self, key: Key):
        mods = pygame.key.get_mods()
        system_mod = mods & pygame.KMOD_CTRL if sys.platform != 'darwin' else mods & pygame.KMOD_META
        if key == pygame.K_BACKSPACE:
            self.active_input_box.backspace()
        elif key == pygame.K_DELETE:
            self.active_input_box.delete()
        elif key == pygame.K_RIGHT:
            self.active_input_box.right()
        elif key == pygame.K_LEFT:
            self.active_input_box.left()
        elif system_mod:
            if key == pygame.K_v:
                text = pyperclip.paste()
                self.active_input_box._value = \
                    self.active_input_box._value[:self.active_input_box.cursor_index] + \
                    [*text] + \
                    self.active_input_box._value[self.active_input_box.cursor_index:]
                self.active_input_box.refresh_text()
                self.active_input_box.cursor_index += len(text)
            elif self.active_input_box.active_selection and key == pygame.K_c:
                pyperclip.copy(self.active_input_box.copy())
            elif self.active_input_box.active_selection and key == pygame.K_x:
                pyperclip.copy(self.active_input_box.copy())
                self.active_input_box.cut()
        elif key.unicode:
            if key.unicode.isalpha() or key.unicode in self.active_input_box.allowed_characters:
                self.active_input_box._value.insert(self.active_input_box.cursor_index, key.unicode)
                self.active_input_box.refresh_text()
                self.active_input_box.cursor_index += 1
            return

    @property
    def cursor_blink(self):
        return time.time() < self.cursor_blink_timer + self.CURSOR_BLINK_STAY

    def push_input_boxes(self):
        self.input_boxes, self.previous_input_boxes = [], self.input_boxes

    def handle_input_boxes(self, _):
        if not self.active_input_box:
            return
        if key := self.key_hold.handle_event():
            if not self.handle_key_action_press(key):
                self.handle_key_action_hold(key)


class ContextualizedInputBoxManager:
    def __init__(self, set_as_context: bool = True):
        self.input_box_manager = StandaloneInputBoxManager()
        if set_as_context:
            settings.game_context = self
