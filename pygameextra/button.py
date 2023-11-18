import time
from typing import Union

from pygameextra import draw, mouse, math, display, settings, recorder
from pygameextra.image import Image
from pygameextra.rect import Rect
from pygameextra.text import Text


def button_lock():
    if not settings.button_lock_enabled: return
    settings.button_lock = time.time()


def hover_lock():
    if not settings.hover_lock_enabled: return
    settings.hover_lock = time.time()


class Button:
    def __init__(self, area: tuple, inactive_resource, active_resource, text: Text = None, hover_action: any = None,
                 hover_data: any = None, action: any = None, data: any = None, disabled: Union[bool, tuple] = False):
        self.area = area
        self.text = text
        self.action = action
        self.data = data
        self.hover_action = hover_action
        self.hover_data = hover_data
        self.disabled = disabled
        self._hovered = False
        self.inactive_resource = inactive_resource
        self.active_resource = active_resource

    def __call__(self, area: tuple = None, inactive_resource=None, active_resource=None, text: Text = None,
                 hover_action: any = None, hover_data: any = None, action: any = None, data: any = None,
                 disabled: Union[bool, tuple] = False):
        self._hovered = self.logic(area or self.area, action or self.action, data or self.data,
                                   hover_action or self.hover_action, hover_data or self.hover_data,
                                   disabled or self.disabled)
        self.render(area or self.area, inactive_resource or self.inactive_resource,
                    active_resource or self.active_resource, self._hovered, disabled or self.disabled)
        self.render_text(area or self.area, text or self.text)

    @staticmethod
    def render(area: tuple, inactive_resource=None, active_resource=None, hovered: bool = False,
               disabled: Union[bool, tuple] = None):
        pass

    @staticmethod
    def render_text(area: tuple, text: Text):
        if not text:
            return
        text.rect.center = math.center(area)
        text.display()

    @staticmethod
    def logic(area, action, data, hover_action, hover_data, disabled: Union[bool, tuple] = None):
        if settings.recording:
            recorder.record(recorder.Button(area, action, data))
        if disabled:
            return
        mouse_rect = Rect(*mouse.pos(), 1, 1)
        button_rect = Rect(*area)
        if button_rect.colliderect(mouse_rect):
            hovered = True
            if (not settings.button_lock) and action and mouse.clicked()[0]:
                button_lock()
                if data is not None:
                    action(data)
                else:
                    action()

            if (not settings.hover_lock) and hover_action:
                hover_lock()
                if hover_data is not None:
                    hover_action(hover_data)
                else:
                    hover_action()
        else:
            hovered = False
        return hovered


class RectButton(Button):
    @staticmethod
    def render(area: tuple, inactive_resource=None, active_resource=None, hovered: bool = False,
               disabled: Union[bool, tuple] = None):
        color = active_resource if (hovered and not disabled) else (
            disabled if type(disabled) == tuple else inactive_resource)
        draw.rect(color, area)


class ImageButton(Button):
    @staticmethod
    def render(area: tuple, inactive_resource=None, active_resource=None, hovered: bool = False,
               disabled: Union[bool, Image] = None):
        image = active_resource if (hovered and not disabled) else (
            disabled if type(disabled) == Image else inactive_resource)
        display.blit(image.surface, (
            area[0] + area[2] * .5 - image.size[0] * .5,
            area[1] + area[3] * .5 - image.size[1] * .5
        ))


def rect(area: tuple, inactive_color: tuple, active_color: tuple, text: Text = None, hover_action: any = None,
         hover_data: any = None, action: any = None, data: any = None, disabled: Union[bool, tuple] = False):
    hovered = Button.logic(area, action, data, hover_action, hover_data, disabled)
    RectButton.render(area, inactive_color, active_color, hovered, disabled)
    RectButton.render_text(area, text)


def image(area: tuple, inactive_image: tuple, active_image: tuple, text: Text = None, hover_action: any = None,
         hover_data: any = None, action: any = None, data: any = None, disabled: Union[bool, Image] = False):
    hovered = Button.logic(area, action, data, hover_action, hover_data, disabled)
    ImageButton.render(area, inactive_image, active_image, hovered, disabled)
    ImageButton.render_text(area, text)