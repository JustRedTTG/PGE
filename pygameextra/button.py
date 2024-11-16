import time
from typing import Union, Hashable, List, Dict

from pygame.rect import RectType

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
    def __init__(self, area: RectType, inactive_resource, active_resource, text: Text = None, hover_action: any = None,
                 hover_data: any = None, action: any = None, data: any = None, hover_draw_action: any = None,
                 hover_draw_data: any = None, disabled: Union[bool, tuple] = False, name: Hashable = None):
        self.area = area
        self.text = text
        self.action = action
        self.data = data
        self.hover_action = hover_action
        self.hover_data = hover_data
        self.hover_draw_action = hover_draw_action
        self.hover_draw_data = hover_draw_data
        self.name = name
        self.disabled = disabled
        self.hovered = False
        self.inactive_resource = inactive_resource
        self.active_resource = active_resource
        self.mouse_offset = settings.spoof_mouse_offset or (0, 0)
        self.display_reference = display.display_reference
        if name is not None and settings.game_context:
            settings.game_context.buttons_with_names[name] = self

    def logic(self, area: RectType = None, hover_action: any = None, hover_data: any = None, action: any = None,
              data: any = None, hover_draw_action: any = None,
              hover_draw_data: any = None, disabled: Union[bool, tuple] = False):
        @display.context_wrap(self.display_reference)
        @mouse.offset_wrap(self.mouse_offset)
        def offset_logic():
            self.hovered = self.static_logic(area or self.area, action or self.action, data or self.data,
                                             hover_action or self.hover_action, hover_data or self.hover_data,
                                             hover_draw_action or self.hover_draw_action,
                                             hover_draw_data or self.hover_draw_data,
                                             disabled or self.disabled)

        offset_logic()

    def check_hover(self, area: RectType = None, disabled: Union[bool, tuple] = False):
        @display.context_wrap(self.display_reference)
        @mouse.offset_wrap(self.mouse_offset)
        def offset_logic():
            self.hovered = self.static_hover_logic(area or self.area, disabled or self.disabled)

        offset_logic()

    def render(self, area: RectType = None, inactive_resource=None, active_resource=None, text: Text = None,
               hover_draw_action: any = None, hover_draw_data: any = None,
               disabled: Union[bool, tuple] = False):
        self.full_static_render(area or self.area, inactive_resource or self.inactive_resource,
                                active_resource or self.active_resource, self.hovered,
                                hover_draw_action or self.hover_draw_action,
                                hover_draw_data or self.hover_draw_data, disabled or self.disabled)
        self.static_render_text(area or self.area, text or self.text)

    def __call__(self, area: RectType = None, inactive_resource=None, active_resource=None, text: Text = None,
                 hover_action: any = None, hover_data: any = None, action: any = None, data: any = None,
                 hover_draw_action: any = None, hover_draw_data: any = None,
                 disabled: Union[bool, tuple] = False):
        self.logic(area, hover_action, hover_data, action, data, hover_draw_action, hover_draw_data, disabled)
        self.render(area, inactive_resource, active_resource, text, hover_draw_action, hover_draw_data, disabled)

    @classmethod
    def full_static_render(cls, area: RectType, inactive_resource=None, active_resource=None, hovered: bool = False,
                           hover_draw_action: any = None, hover_draw_data: any = None,
                           disabled: Union[bool, tuple] = None):
        if not (settings.do_not_render_if_hover_draw and hover_draw_action and hovered):
            cls.static_render(area, inactive_resource, active_resource, hovered, disabled)
        if hover_draw_action and hovered:
            cls.static_do_hover_action(hover_draw_action, hover_draw_data)

    @staticmethod
    def static_render(area: RectType, inactive_resource=None, active_resource=None, hovered: bool = False,
                      disabled: Union[bool, tuple] = None):
        pass

    @staticmethod
    def static_render_text(area: RectType, text: Text):
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
    def static_logic(area, action, data, hover_action, hover_data, hover_draw_action: any = None,
                     hover_draw_data: any = None, disabled: Union[bool, tuple] = None) -> bool:
        if disabled:
            return False
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

            Button.static_do_hover_action(hover_draw_action, hover_draw_data)
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
    def static_render(area: RectType, inactive_resource=None, active_resource=None, hovered: bool = False,
                      disabled: Union[bool, tuple] = None):
        color = active_resource if (hovered and not disabled) else (
            disabled if type(disabled) is tuple else inactive_resource)
        draw.rect(color, area)


class ImageButton(Button):
    @staticmethod
    def static_render(area: RectType, inactive_resource=None, active_resource=None, hovered: bool = False,
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
    if button.name is not None and \
            (previous_button := settings.game_context.previous_buttons_with_names.get(button.name, None)) is not None:
        button.hovered = previous_button.hovered
        button.render()
        button.hovered = False
    elif settings.raise_error_for_button_without_name and button.name is None:
        raise ValueError(
            "The pygameextra settings demand that all buttons have a name, "
            "trace the button and give it a name to avoid this error."
        )
    elif settings.use_button_context_indexing and len(settings.game_context.previous_buttons) >= (
            buttons_length := len(settings.game_context.buttons)):
        button.hovered = settings.game_context.previous_buttons[buttons_length - 1].hovered
        button.render()
        button.hovered = False
    elif not settings.use_button_context_indexing:
        button.hovered = button.static_hover_logic(button.area, button.disabled)
        if button.hovered:
            button.static_do_hover_action(button.hover_action, button.hover_data)
            button.render()
    else:
        button.hovered = False
        button.render()


def action(area: RectType, text: Text = None, hover_action: any = None,
           hover_data: any = None, action: any = None, data: any = None, hover_draw_action: any = None,
           hover_draw_data: any = None, disabled: Union[bool, tuple] = False, name: Hashable = None):
    if settings.game_context:
        button = Button(
            area, None, None,
            text, hover_action, hover_data, action, data, hover_draw_action, hover_draw_data, disabled, name)
        settings.game_context.buttons.append(button)
        check_hover(button)
        return
    hovered = Button.static_logic(area, action, data, hover_action, hover_data, hover_draw_action, hover_draw_data,
                                  disabled)
    Button.static_render_text(area, text)


def rect(area: RectType, inactive_color: tuple, active_color: tuple, text: Text = None, hover_action: any = None,
         hover_data: any = None, action: any = None, data: any = None, hover_draw_action: any = None,
         hover_draw_data: any = None, disabled: Union[bool, tuple] = False, name: Hashable = None):
    if settings.game_context:
        button = RectButton(area, inactive_color, active_color, text, hover_action, hover_data, action, data,
                            hover_draw_action, hover_draw_data, disabled, name)
        settings.game_context.buttons.append(button)
        check_hover(button)
        return
    hovered = Button.static_logic(area, action, data, hover_action, hover_data, hover_draw_action, hover_draw_data,
                                  disabled)
    RectButton.full_static_render(area, inactive_color, active_color, hovered, hover_draw_action, hover_draw_data,
                                  disabled)
    RectButton.static_render_text(area, text)


def image(area: RectType, inactive_image: tuple, active_image: tuple, text: Text = None, hover_action: any = None,
          hover_data: any = None, action: any = None, data: any = None, hover_draw_action: any = None,
          hover_draw_data: any = None, disabled: Union[bool, Image] = False, name: Hashable = None):
    if settings.game_context:
        button = ImageButton(area, inactive_image, active_image, text, hover_action, hover_data, action, data,
                             hover_draw_action, hover_draw_data, disabled, name)
        settings.game_context.buttons.append(button)
        check_hover(button)
        return
    hovered = Button.static_logic(area, action, data, hover_action, hover_data, hover_draw_action, hover_draw_data,
                                  disabled)
    ImageButton.static_render(area, inactive_image, active_image, hovered, disabled)
    ImageButton.static_render_text(area, text)


class ButtonManager:
    def __init__(self, set_as_context: bool = True):
        self.buttons: List[Button] = []
        self.buttons_with_names: Dict[Hashable, Button] = {}
        self.previous_buttons: List[Button] = []
        self.previous_buttons_with_names: Dict[Hashable, Button] = {}
        if set_as_context:
            settings.game_context = self

    def handle_buttons(self):
        for button in reversed(self.buttons):
            button.logic()
            if button.hovered:
                break

    def push_buttons(self):
        self.buttons, self.previous_buttons = [], self.buttons
        self.buttons_with_names, self.previous_buttons_with_names = {}, self.buttons_with_names
