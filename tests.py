import random

import pygameextra as pe
from pygameextra import settings
from pygameextra.debug import FreeMode
from pygameextra.fpslogger import Logger
from pygameextra import fingersupport
if pe.version.VERSION == '2.0.0' and pe.version.revision >= 4:
    pass
else:
    print('Please use 2.0.0b4 or later')
    exit()
pe.init()

pe.display.make((700, 600), "Cool", pe.display.DISPLAY_MODE_RESIZABLE)

log = Logger(size=20)
log.render()
pe.settings.debugger = FreeMode()
settings.button_lock_timeout_time = 0
settings.button_lock_hold = False

draggable = pe.mouse.Draggable((5, 5), (150, 150), True)

while True:
    for pe.event.c in pe.event.get():
        pe.event.quitCheckAuto()
        fingersupport.handle_finger_events()
    # pe.fill.full(pe.colors.verydarkgray)
    pe.fill.full(pe.colors.white)

    pe.start_recording()

    _, pos = draggable.check()
    pe.draw.rect(pe.colors.gray, (*pos, *draggable.area), 0)

    log.render()
    pe.display.update()
    pe.stop_recording()
    if pe.mouse.clicked()[2]:
        pe.start_debug()