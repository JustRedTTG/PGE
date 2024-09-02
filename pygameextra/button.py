import time
from typing import Union

from pygameextra import draw, mouse, math, display, settings, colors
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
        self.hovered = False
        self.inactive_resource = inactive_resource
        self.active_resource = active_resource
        self.mouse_offset = settings.spoof_mouse_offset or (0, 0)
        self.display_reference = display.display_reference

    def logic(self, area: tuple = None, hover_action: any = None, hover_data: any = None, action: any = None,
              data: any = None, disabled: Union[bool, tuple] = False):
        @display.context_wrap(self.display_reference)
        @mouse.offset_wrap(self.mouse_offset)
        def offset_logic():
            self.hovered = self.static_logic(area or self.area, action or self.action, data or self.data,
                                             hover_action or self.hover_action, hover_data or self.hover_data,
                                             disabled or self.disabled)
        offset_logic()

    def check_hover(self, area: tuple = None, disabled: Union[bool, tuple] = False):
        @display.context_wrap(self.display_reference)
        @mouse.offset_wrap(self.mouse_offset)
        def offset_logic():
            self.hovered = self.static_hover_logic(area or self.area, disabled or self.disabled)

        offset_logic()

    def render(self, area: tuple = None, inactive_resource=None, active_resource=None, text: Text = None,
               disabled: Union[bool, tuple] = False):

        self.static_render(area or self.area, inactive_resource or self.inactive_resource,
                           active_resource or self.active_resource, self.hovered, disabled or self.disabled)
        self.static_render_text(area or self.area, text or self.text)

    def __call__(self, area: tuple = None, inactive_resource=None, active_resource=None, text: Text = None,
                 hover_action: any = None, hover_data: any = None, action: any = None, data: any = None,
                 disabled: Union[bool, tuple] = False):
        self.logic(area, hover_action, hover_data, action, data, disabled)
        self.render(area, inactive_resource, active_resource, text, disabled)

    @staticmethod
    def static_render(area: tuple, inactive_resource=None, active_resource=None, hovered: bool = False,
                      disabled: Union[bool, tuple] = None):
        pass

    @staticmethod
    def static_render_text(area: tuple, text: Text):
        if not text:
            return
        text.rect.center = math.center(area)
        text.display()

    @staticmethod
    def static_hover_logic(area, disabled: Union[bool, tuple] = None) -> bool:
        if disabled:
            return False
        mouse_rect = Rect(*mouse.pos(), 1, 1)
        button_rect = Rect(*area)
        return button_rect.colliderect(mouse_rect)


    @staticmethod
    def static_logic(area, action, data, hover_action, hover_data, disabled: Union[bool, tuple] = None):
        if disabled:
            return
        if Button.static_hover_logic(area, disabled):
            hovered = True
            if (not settings.button_lock) and action and mouse.clicked()[0]:
                button_lock()
                if data is not None:
                    if type(data) is tuple:
                        action(*data)
                    else:
                        action(data)
                else:
                    action()

            Button.static_do_hover_action(hover_action, hover_data)
        else:
            hovered = False
        return hovered

    def do_hover_action(self):
        @display.context_wrap(self.display_reference)
        @mouse.offset_wrap(self.mouse_offset)
        def offset_hover_action():
            self.static_do_hover_action(self.hover_action, self.hover_data)

        offset_hover_action()

    @staticmethod
    def static_do_hover_action(hover_action, hover_data):
        if (not settings.hover_lock) and hover_action:
            hover_lock()
            if hover_data is not None:
                if type(hover_data) is tuple:
                    hover_action(*hover_data)
                else:
                    hover_action(hover_data)
            else:
                hover_action()


class RectButton(Button):
    @staticmethod
    def static_render(area: tuple, inactive_resource=None, active_resource=None, hovered: bool = False,
                      disabled: Union[bool, tuple] = None):
        color = active_resource if (hovered and not disabled) else (
            disabled if type(disabled) is tuple else inactive_resource)
        draw.rect(color, area)


class ImageButton(Button):
    @staticmethod
    def static_render(area: tuple, inactive_resource=None, active_resource=None, hovered: bool = False,
                      disabled: Union[bool, Image] = None):
        image = active_resource if (hovered and not disabled) else (
            disabled if isinstance(disabled, Image) else inactive_resource)
        display.blit(image.surface, (
            area[0] + area[2] * .5 - image.size[0] * .5,
            area[1] + area[3] * .5 - image.size[1] * .5
        ))


def check_hover(button: Button):
    if not settings.game_context:
        return
    if Button.static_hover_logic(button.area, button.disabled):
        button.hovered = True
        Button.static_do_hover_action(button.hover_action, button.hover_data)
    button.render()


def action(area: tuple, text: Text = None, hover_action: any = None,
           hover_data: any = None, action: any = None, data: any = None, disabled: Union[bool, tuple] = False):
    if settings.game_context:
        button = Button(area, None, None, text, hover_action, hover_data, action, data, disabled)
        settings.game_context.buttons.append(button)
        check_hover(button)
        return
    hovered = Button.static_logic(area, action, data, hover_action, hover_data, disabled)
    Button.static_render_text(area, text)


def rect(area: tuple, inactive_color: tuple, active_color: tuple, text: Text = None, hover_action: any = None,
         hover_data: any = None, action: any = None, data: any = None, disabled: Union[bool, tuple] = False):
    if settings.game_context:
        button = RectButton(area, inactive_color, active_color, text, hover_action, hover_data, action, data, disabled)
        settings.game_context.buttons.append(button)
        check_hover(button)
        return
    hovered = Button.static_logic(area, action, data, hover_action, hover_data, disabled)
    RectButton.static_render(area, inactive_color, active_color, hovered, disabled)
    RectButton.static_render_text(area, text)


def image(area: tuple, inactive_image: tuple, active_image: tuple, text: Text = None, hover_action: any = None,
          hover_data: any = None, action: any = None, data: any = None, disabled: Union[bool, Image] = False):
    if settings.game_context:
        button = ImageButton(area, inactive_image, active_image, text, hover_action, hover_data, action, data, disabled)
        settings.game_context.buttons.append(button)
        check_hover(button)
        return
    hovered = Button.static_logic(area, action, data, hover_action, hover_data, disabled)
    ImageButton.static_render(area, inactive_image, active_image, hovered, disabled)
    ImageButton.static_render_text(area, text)
