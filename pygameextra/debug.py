from pygameextra import display, fill, draw, colors, event, mouse
from pygameextra.fpslogger import Logger


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
            if event.quit_check():
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
