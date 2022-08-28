import random

import pygameextra as pe
from pygameextra import settings
from pygameextra.debug import FreeMode
from pygameextra.fpslogger import Logger
print(pe.__version__)
pe.init()

pe.display.make((500, 500), "Cool", pe.display.DISPLAY_MODE_RESIZABLE)

log = Logger(size=20)
pe.settings.debugger = FreeMode()
settings.button_timeout_time = 0
settings.button_lock_hold = False

class Cube:
    def __init__(self, size, location, color=pe.colors.white):
        self.size = size
        self.loc = location
        self.draggable = pe.mouse.Draggable(location, self.size)
        self.color = color
        self.fake = None
        self.click = None
        self.target = (0, 0)

    def draw(self):
        pe.draw.rect(self.color, (*self.loc, *self.size))

    def call(self):
        if self.fake:
            settings.mouse_position = self.fake
            settings.mouse_clicked = [True, 0, 0]
        mov, pos = self.draggable.check()
        self.loc = pos
        if self.fake:
            if pe.math.dist(self.loc, self.target) <= 5:
                self.fake = None
                self.click = None
            else:
                self.fake = pe.math.lerp(self.fake, self.target, .1)
        return mov

    def target_m(self, place):
        self.target = place
        self.fake = (self.loc[0]+2, self.loc[1]+2)

cubes = []
x = 0
y = 0
ligma = 50
ranging = ligma ** 2


def normalize(start = 0, end = 0, fitmin = 0, fitmax = 255, value = 0):
    n = (value - start) / (end - start)
    return fitmin + n * (fitmax - fitmin)


for i in range(ligma):
    for i1 in range(ligma):
        r = normalize(0, ranging, 100, 255, i*i1)
        g = normalize(0, ranging, 50, 100, i*i1)
        b = normalize(0, ranging, 60, 255, i*i1)
        cubes.append(Cube((10, 10), (x, y), (r, g, b)))
        y += 10
    x += 10
    y = 0

while True:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    pe.start_recording()
    pe.fill.full(pe.colors.verydarkgray)

    for cube in cubes:
        cube.draw()
    cubes.reverse()
    log.resetwatch('call')
    settings.enable_spoof = True
    for cube in cubes:
        mov = cube.call()
        pe.event.buttonLocking()
        if mov:
            cubes.remove(cube)
            cubes.insert(0, cube)
    settings.enable_spoof = False
    log.stopwatch('call')
    cubes.reverse()

    for cube in cubes:
        if cube.fake: continue
        cube.target_m((random.randint(0, 500), random.randint(0, 500)))

    log.render()
    pe.display.update()
    pe.stop_recording()
    if pe.mouse.clicked()[2]:
        pe.start_debug()
