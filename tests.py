import random

import pygameextra as pe
from pygameextra import settings
from pygameextra.debug import FreeMode
from pygameextra.fpslogger import Logger
if pe.version.VERSION == '2.0.0' and pe.version.revision >= 4:
    pass
else:
    print('Please use 2.0.0b4 or later')
    exit()
pe.init()

pe.display.make((700, 700), "Cool", pe.display.DISPLAY_MODE_RESIZABLE)

log = Logger(size=20)
log.render()
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
                self.fake = pe.math.lerp(self.fake, self.target, (1/pe.math.dist(self.fake, self.target))*10)
        return mov

    def target_m(self, place):
        self.target = place
        self.fake = (self.loc[0], self.loc[1])

cubes = []
x = 0
y = 0
ligma = 10
ranging = ligma ** 2


def normalize(start = 0, end = 0, fitmin = 0, fitmax = 255, value = 0):
    n = (value - start) / (end - start)
    return fitmin + n * (fitmax - fitmin)

s = 2

for i in range(ligma):
    for i1 in range(ligma):
        r = normalize(0, ranging, 100, 255, i*i1)
        g = normalize(0, ranging, 50, 100, i*i1)
        b = normalize(0, ranging, 60, 255, i*i1)
        cubes.append(Cube((s, s), (x, y), (r, g, b)))
        y += s
    x += s
    y = 0

points = []

x, y = 0, 0
d = 9
for _ in range(d+1):
    for _ in range(d+1):
        points.append((x, y))
        x += 700/d
    x = 0
    y += 700/d

transI = 0

while True:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    #pe.start_recording()
    if transI >= 1:
        pe.fill.transparency(pe.colors.black, 1)
        transI = 0

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
        cube.target_m(random.choice(points))
    pe.draw.rect(pe.colors.black, (10, pe.display.get_height() - 10 - log.font.get_height(), *log.surface.get_size()))
    log.render()
    pe.display.update()
    #pe.stop_recording()
    if pe.mouse.clicked()[2]:
        pe.start_debug()
    transI += 1