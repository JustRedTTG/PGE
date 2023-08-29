from pygameextra import display, fill, draw, settings, colors, event, mouse, recorder, button
from pygameextra.fpslogger import Logger
from pygameextra.rect import Rect


class Debugger:
    log = None
    active = True
    reactivate = False
    reactivate_init = False
    target = None
    display_backup = None
    draggable = None
    offset = (0, 0)
    offset2 = (0, 0)
    start_mouse_position = (0, 0)
    start_enable_spoof = True
    start_mouse_position_spoof = None

    def __init__(self):
        self.make_logger()

    def make_logger(self):
        self.log = Logger()

    def setup_display(self):
        mon_size = display.get_max()
        display.make((min(self.target.size[0] * 2, mon_size[0]), min(self.target.size[1] * 2, mon_size[1])), 'DEBUG',
                     display.DISPLAY_MODE_RESIZABLE)

    def before_run(self):
        # noinspection PyArgumentList
        self.target = display.display_reference.copy()
        self.display_backup = display.backup_details()
        self.setup_display()
        self.offset = (
            self.target.size[0] * .5,
            self.target.size[1] * .5
        )
        self.draggable = mouse.Draggable(self.offset)

    def reset(self):
        del self.target
        del self.display_backup
        if not self.reactivate:
            del self.draggable
        self.active = True

    def after_run(self):
        if not self.reactivate:
            display.make(*self.display_backup)
        display.display_reference.size = self.display_backup[0]

    def after_update(self):
        pass

    def update(self):
        for event.c in event.get():
            if event.quitCheck():
                self.active = False
        fill.full(colors.verydarkgray)
        fill.interlace(colors.pge_light, max(int(display.get_width() * .03), 3))
        movement, new_pos = self.draggable.check()

        self.offset = new_pos
        display.blit(self.target, self.offset)

        if self.log.count > 1:
            draw.polygon(colors.pge_dark, [
                (0, display.get_height()),
                (106, display.get_height()),
                (53, display.get_height() - 43),
                (0, display.get_height() - 43),
            ], 0)
            draw.polygon(colors.verydarkgray, [
                (0, display.get_height()),
                (100, display.get_height()),
                (50, display.get_height() - 40),
                (0, display.get_height() - 40),
            ], 0)
        else:
            fill.transparency(colors.black, 200)
        self.log.render()
        self.after_update()
        display.update(60)


class FreeMode(Debugger):
    def before_run(self):
        self.target = recorder.reconstruct(settings.recording_data)
        self.display_backup = display.backup_details()
        self.setup_display()
        if not self.reactivate_init:
            self.offset = (
                display.get_width() * .5 - self.target.size[0] * .5,
                display.get_height() * .5 - self.target.size[1] * .5
            )
        if not self.reactivate_init:
            self.draggable = mouse.Draggable(self.offset)
            settings.button_lock = False
        else:
            button.button_lock()


class FreeInteractMode(FreeMode):
    def after_update(self):
        mouse_rect = Rect(*mouse.pos(False), 1, 1)
        self.draggable.lock = False
        for item in settings.recording_data:
            if type(item) == recorder.Portion:
                if self.reactivate_init:
                    old = self.offset2
                self.offset2 = item.x, item.y
                if self.reactivate_init:
                    if old != self.offset2:
                        nudge = (self.offset2[0] - old[0], self.offset2[1] - old[1])
                        self.offset = (self.offset[0] - nudge[0], self.offset[1] - nudge[1])
                        self.draggable.pos = self.offset
                    self.reactivate_init = False
            elif type(item) == recorder.Button:
                area = (
                item.area[0] + self.offset[0] + self.offset2[0], item.area[1] + self.offset[1] + self.offset2[1],
                item.area[2], item.area[3])
                button_rect = Rect(*area)
                if button_rect.colliderect(mouse_rect):
                    draw.rect(colors.green, area, 2)
                    self.draggable.lock = True
                    if (not settings.button_lock) and item.action and mouse.clicked(False)[0]:
                        button.button_lock()
                        if item.data is None:
                            item.action()
                        else:
                            item.action(item.data)
                        self.active = False
                        self.reactivate = True
                elif not settings.button_lock:
                    draw.rect(colors.black, area, 3)
                    draw.rect(colors.red, area, 1)
