import random

import pygameextra as pe
from pygameextra.fpslogger import logger

pe.init()

pe.display.make((250, 250), "Cool", pe.display.DISPLAY_MODE_RESIZABLE)

sprite = pe.Sprite('image.jpg', (20, 20))

log = logger('font.ttf', 20, (10, 220))

while True:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    pe.fill.full((0, 0, 0))
    for _ in range(100):
        sprite.display((random.randint(0, 240), random.randint(0, 240)))
    log.render()
    pe.display.update(200)
