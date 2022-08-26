import pygameextra.version
import pygameextra as pe
from pygameextra.debug import FreeMode
from pygameextra.fpslogger import Logger
print(pe.__version__)
pe.init()

pe.display.make((250, 250), "Cool", pe.display.DISPLAY_MODE_RESIZABLE)

sprite = pe.Sprite('image.jpg', (25, 25))
big_sprite = pe.Sprite('image.jpg', (250, 250))

log = Logger(size=20)
pe.settings.debugger = FreeMode()
while True:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    pe.start_recording()
    pe.fill.interlace((255, 0, 0), 3)
    big_sprite.display((-50, -20))
    log.render()
    pe.display.update(200)
    pe.stop_recording()
    if pe.mouse.clicked()[2]:
        pe.start_debug()
