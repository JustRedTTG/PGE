import time
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


def rect(area: tuple, inactive_color: tuple, active_color: tuple, text: Text = None, hover_action: any = None,
         hover_data: any = None, action: any = None, data: any = None, disabled: [bool, tuple] = False):
    if disabled:
        if type(disabled) == bool:
            draw.rect(active_color, area)
        else:
            # noinspection PyTypeChecker
            draw.rect(disabled, area)
        if text:
            text.rect.center = math.center(area)
            text.display()
        if settings.recording:
            recorder.record(recorder.Button(area, action, data))
        return
    mouse_rect = Rect(*mouse.pos(), 1, 1)
    button_rect = Rect(*area)
    if button_rect.colliderect(mouse_rect):
        draw.rect(active_color, area)
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
        draw.rect(inactive_color, area)
    if settings.recording:
        recorder.record(recorder.Button(area, action, data))
    if not text:
        return
    text.rect.center = math.center(area)
    text.display()


def image(area: tuple, inactive_image: Image, active_image: Image, action: any = None, data: any = None,
          disabled: bool = False):
    if disabled:
        if type(disabled) == bool:
            display.blit(active_image.surface, (
                area[0] + area[2] * .5 - active_image.size[0] * .5,
                area[1] + area[3] * .5 - active_image.size[1] * .5
            ))
        else:
            display.blit(inactive_image.surface, (
                area[0] + area[2] * .5 - inactive_image.size[0] * .5,
                area[1] + area[3] * .5 - inactive_image.size[1] * .5
            ))
        if settings.recording:
            recorder.record(recorder.Button(area, action, data))
        return
    mouse_rect = Rect(*mouse.pos(), 1, 1)
    button_rect = Rect(*area)
    if button_rect.colliderect(mouse_rect):
        display.blit(active_image.surface, (
            area[0] + area[2] * .5 - active_image.size[0] * .5,
            area[1] + area[3] * .5 - active_image.size[1] * .5
        ))
        if (not settings.button_lock) and action and mouse.clicked()[0]:
            button_lock()
            if data is not None:
                action(data)
            else:
                action()
    else:
        display.blit(inactive_image.surface, (
            area[0] + area[2] * .5 - inactive_image.size[0] * .5,
            area[1] + area[3] * .5 - inactive_image.size[1] * .5
        ))

    if not settings.recording:
        return
    recorder.record(recorder.Button(area, action, data))
