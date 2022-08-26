from pygameextra import draw, mouse, math, display, settings, recorder
from pygameextra.rect import Rect
from pygameextra.text import Text


def rect(area: tuple, inactive_color: tuple, active_color: tuple, text: Text = None, action: any = None, data: any = None, disabled: [bool, tuple] = False):
    if disabled:
        if type(disabled) == bool:
            draw.rect(active_color, area)
        else:
            draw.rect(disabled, area)
        text.rect.center = math.center(area)
        text.display()
        return
    mouse_rect = Rect(*mouse.pos(), 1, 1)
    button_rect = Rect(*area)
    if button_rect.colliderect(mouse_rect):
        draw.rect(active_color, area)
        if action and mouse.clicked()[0]:
            if data != None:
                action(data)
            else:
                action()
    else:
        draw.rect(inactive_color, area)
    if settings.recording:
        recorder.record(recorder.Button(area, action, data))
    if not text:
        return
    text.rect.center = math.center(area)
    text.display()


def image(area: tuple, inactive_image: tuple, active_image: tuple, action=None, data=None):
    mouse_rect = Rect(*mouse.pos(), 1, 1)
    button_rect = Rect(*area)
    if button_rect.colliderect(mouse_rect):
        display.blit(active_image.surface, (
            area[0] + area[2]*.5 - active_image.size[0]*.5,
            area[1] + area[3]*.5 - active_image.size[1]*.5
        ))
        if action and mouse.clicked()[0]:
            if data != None:
                action(data)
            else:
                action()
    else:
        display.blit(inactive_image.surface, (
            area[0] + area[2]*.5 - inactive_image.size[0]*.5,
            area[1] + area[3]*.5 - inactive_image.size[1]*.5
        ))

    if not settings.recording:
        return
    recorder.record(recorder.Button(area, action, data))