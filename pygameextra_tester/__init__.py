import os
import pygameextra as pe
from pygameextra.debug import FreeInteractMode
from pygameextra.fpslogger import Logger
from pygameextra import settings

pe.init()
pe.display.make((500, 500), "PGE Testing Utility", 0)
sp = os.path.dirname(os.path.realpath(__file__))

# Button images
bX = pe.Image(f"{sp}/Xbutton.png", size=(100, 100), position=(100, 0))
bX2 = pe.Image(f"{sp}/Xbutton.png", size=(20, 20), position=(100, 0))
sX = pe.Image(f"{sp}/Xbutton.png", size=(20, 20), position=(100, 0))
bY = pe.Image(f"{sp}/Ybutton.png", size=(100, 100), position=(100, 0))
bY2 = pe.Image(f"{sp}/Ybutton.png", size=(20, 20), position=(100, 0))

# Sprite sheet sprites
s1 = pe.Sprite(pe.Sheet(f"{sp}/rows.png", pe.SheetHorizontal(16, 16)), (250, 250), (0, 0),
               pivot="topleft")  # Rows sprite
s2 = pe.Sprite(pe.Sheet(f"{sp}/columns.png", pe.SheetVertical(32, 32)), (250, 250), (250, 0),
               pivot="topleft")  # Columns sprite

# Resized sprites
s3 = pe.Sprite(f"{sp}/mario_01.png", (250, 250), pe.math.center((0, 250, 125, 125)))  # Resized sprite 1
s3.size = 0.5

s4 = pe.Sprite(f"{sp}/mario_01.png", (250, 250), pe.math.center((125, 250, 125, 125)))  # Resized sprite 2
s4.size = 0.25

s5 = pe.Sprite(f"{sp}/mario_01.png", (250, 250), pe.math.center((0, 375, 125, 125)))  # Resized sprite 3
s5.size = 0.1

s6 = pe.Sprite(f"{sp}/mario_01.png", (250, 250), pe.math.center((125, 375, 125, 125)))  # Resized sprite 4
s6.size = 0.05

s7 = pe.Sprite(f"{sp}/mario_01.png", (250, 250), pe.math.center((250, 250, 250, 250)), 90,
               pivot="center")  # Rotated sprite

mouse_icon = pe.Image(f'{sp}/mouse_middle.png', (50, 50))
debug_icon = pe.Image(f'{sp}/debug_icon.png', (50, 50))

# Init sprites
# s1.init()
# s2.init()
# s3.init()
# s4.init()
# s5.init()
# s6.init()
# s7.init()

# Setup some more things...
bt = {  # Button texts
    'button': pe.text.quick('Buttons', 15, pe.math.center((0, 200, 100, 50))),
    'slider': pe.text.quick('Sliders', 15, pe.math.center((100, 200, 100, 50))),
    'back': pe.text.quick('< Back', 15, pe.math.center((0, 0, 100, 50))),
    'sprite': pe.text.quick('Sprites', 15, pe.math.center((200, 200, 100, 50))),
    'shapes': pe.text.quick('Shapes', 15, pe.math.center((300, 200, 100, 50))),
    'mapping': pe.text.quick('Mapping', 15, pe.math.center((300, 250, 100, 50))),
    'math': pe.text.quick('Math', 15, pe.math.center((400, 200, 100, 50))),
    'math_lerp': pe.text.quick('Lerp', 15, pe.math.center((0, 200, 100, 50))),
    'math_center': pe.text.quick('Center', 15, pe.math.center((100, 200, 100, 50))),
    'math_dist': pe.text.quick('Distance', 15, pe.math.center((200, 200, 100, 50))),
    'math_tsx': pe.text.quick('TSX', 15, pe.math.center((300, 200, 100, 50))),
    'math_back': pe.text.quick('< Math', 15, pe.math.center((0, 0, 100, 50))),
    '+': pe.text.quick('+', 15, pe.math.center((275, 200, 50, 50))),
    '-': pe.text.quick('-', 15, pe.math.center((175, 200, 50, 50))),
    'lerplength': pe.text.quick("100", 15, pe.math.center((225, 200, 50, 50))),
    'distance': pe.text.quick("100", 15, pe.math.center((225, 200, 50, 50))),
    'tsx_radius': pe.text.quick("100", 15, pe.math.center((225, 145, 50, 50))),
    'tsx_segments': pe.text.quick("100", 15, pe.math.center((225, 200, 50, 50))),
    'tsx_offset': pe.text.quick("100", 15, pe.math.center((225, 255, 50, 50))),
    'debug_label': pe.text.quick("Open Debug", 15, pe.math.center((400, 440, 90, 50))),
    'debug_close': pe.text.quick("Close Debug", 15, pe.math.center((400, 440, 90, 50)))
}
bt['math_back'].color = pe.colors.white
bt['math_back'].init()
bt['lerplength'].color = pe.colors.white
bt['lerplength'].init()
bt['tsx_radius'].color = pe.colors.white
bt['tsx_radius'].init()
bt['tsx_segments'].color = pe.colors.white
bt['tsx_segments'].init()
bt['tsx_offset'].color = pe.colors.white
bt['tsx_offset'].init()
bt['debug_label'].color = pe.colors.white
bt['debug_label'].init()
bt['debug_close'].color = pe.colors.white
bt['debug_close'].init()
s1.speed = .1  # Set sprite animation
s2.speed = .2  # Set sprite animation
s2.pong = True  # Enable sprite pong
sO = 50  # Set slider variable
sT = 50  # Set slider variable
test = ""
testall = 0
testdrop = -100
lerplength = .5
tsx_segments = 100
tsx = pe.TSX((250, 250), 100)
log = Logger()


# Button function
def set_test(data):
    global test
    test = data
    if "math_" in data and not data == "math_tsx":
        settings.button_lock_timeout_time = .2
        settings.button_lock_hold = False
        pe.display.make((500, 500), "PGE Testing Utility", 1)
    else:
        settings.button_lock_timeout_time = .1
        settings.button_lock_hold = True
        pe.display.make((500, 500), "PGE Testing Utility", 0)


def set_lerplength(data):
    global lerplength
    lerplength = data


def set_tsx_radius(data):
    global tsx
    tsx.radius = data


def set_tsx_segments(data):
    global tsx_segments
    tsx_segments = data


def set_tsx_offset(data):
    global tsx
    tsx.offset = data


# Test functions
testscore = 0

pe.settings.debugger = FreeInteractMode()


# Main GAME LOOP
# noinspection PyTypeChecker
def run():
    global sO, sT
    while True:
        for pe.event.c in pe.event.get():
            pe.event.quitCheckAuto()
        pe.start_recording()
        pe.fill.full(pe.colors.verydarkgray)

        debug_icon.display((350, 440))
        bt['debug_close'].display()

        settings.recording = False
        pe.draw.rect(pe.colors.verydarkgray, (350, 440, 150, 60))
        settings.recording = True

        if test == "slider":
            # noinspection PyShadowingNames
            sO = pe.slider.boxed((125, 100, 250, 15, 20), (255, 0, 0), 0, 100, sO, (0, 0, 255), (0, 0, 0), (0, 255, 0),
                                 True, (0, 0, 255))
            # noinspection PyShadowingNames
            sT = pe.slider.normal((125, 150, 250, 15, 20), sX, 0, 100, sT, (255, 255, 255), (0, 255, 0), 5, True,
                                  (0, 0, 255), 3)
        elif test == "button":
            midpoint = pe.display.get_width() * .5 - 100
            midheight = pe.display.get_height() * .5 - 50
            x = 0
            y = 0
            while x < 99 and y < 99:
                # bX2.position = (x+150, y+200)
                # bX2.rect = bX2.object.get_rect(topleft=(x+150, y+200))
                # bY2.position = (x + 150, y + 200)
                # bY2.rect = bY2.object.get_rect(topleft=(x + 150, y + 200))
                pe.button.rect((x + midpoint, y + midheight, 20, 20), pe.colors.red, pe.colors.green)
                pe.button.image((x + midpoint + 100, y + midheight, 20, 20), bX2, bY2)
                x += 20
                if x > 99:
                    x = 0
                    y += 20
        elif test == "sprite":
            pe.comment('Sprites')
            s1.display()
            s2.display()
            pe.padding_comment()
            # s3.display()
            # s4.display()
            # s5.display()
            # s6.display()
            # s7.display()
        elif test == "mapping":
            pe.display.blit(s1.reference.surface, (202, 218))
            for id in list(s1.reference.handler.mapping):
                rect = s1.reference.handler.mapping[id]
                pe.draw.rect(pe.colors.red, (rect[0] + 202, rect[1] + 218, rect[2], rect[3]), 1)
            pe.display.blit(s2.reference.surface, (122, 250))
            for id in list(s2.reference.handler.mapping):
                rect = s2.reference.handler.mapping[id]
                pe.draw.rect(pe.colors.green, (rect[0] + 122, rect[1] + 250, rect[2], rect[3]), 1)
        elif test == "shapes":
            pe.draw.circle(pe.colors.red, (125, 125), 50, 5)
            pe.draw.circle(pe.colors.aqua, (125, 125), 40, 0)
            pe.draw.rect(pe.colors.red, (325, 75, 100, 100), 5)
            pe.draw.rect(pe.colors.aqua, (335, 85, 80, 80), 0)
            pe.draw.line(pe.colors.red, (0, 250), (250, 500), 5)
            pe.draw.line(pe.colors.red, (250, 250), (0, 500), 5)
            pe.draw.ellipse(pe.colors.red, (250, 250, 250, 250))

        if test == "":
            pe.button.rect((0, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt['button'], action=set_test,
                           data="button")
            pe.button.rect((100, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt['slider'], action=set_test,
                           data="slider", disabled=pe.colors.gray)
            pe.button.rect((200, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt['sprite'], action=set_test,
                           data="sprite")
            pe.button.rect((200, 250, 100, 50), pe.colors.white, pe.colors.lightgray, bt['mapping'], action=set_test,
                           data="mapping")
            pe.button.rect((300, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt['shapes'], action=set_test,
                           data="shapes")
            pe.button.rect((400, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt['math'], action=set_test,
                           data="math")

            settings.recording = False
            mouse_icon.display((350, 440))
            bt['debug_label'].display()
            settings.recording = True

        elif test == "math":
            pe.button.rect((0, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt['math_lerp'], action=set_test,
                           data="math_lerp")
            pe.button.rect((100, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt['math_center'],
                           action=set_test, data="math_center")
            pe.button.rect((200, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt['math_dist'], action=set_test,
                           data="math_dist")
            pe.button.rect((300, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt['math_tsx'], action=set_test,
                           data="math_tsx")
        if test != "":
            if "math_" in test:
                pe.button.rect((0, 0, 100, 50), pe.colors.verydarkgray, pe.colors.darkgray, bt['math_back'],
                               action=set_test, data="math")
            elif test == "testall":
                pass
            else:
                pass
                pe.button.rect((0, 0, 100, 50), pe.colors.white, pe.colors.lightgray, bt['back'], action=set_test,
                               data="")
            #

        if test == "math_lerp":
            if pe.display.get_width() < 325 or pe.display.get_height() < 250:
                x, y = 0, 0
                s = pe.display.get_size()
                while s[0] + x < 325 or s[1] + y < 250:
                    if s[0] + x < 325:
                        x += 1
                    if s[1] + y < 250:
                        y += 1
                pe.display.make((s[0] + x, s[1] + y), "PGE Testing Utility", 1)
            pe.button.rect((175, 200, 50, 50), pe.colors.gray, pe.colors.darkgray, bt['-'], set_lerplength,
                           lerplength - .1)
            bt['lerplength'].text = f'{lerplength:.1f}'
            bt['lerplength'].init()
            bt['lerplength'].display()
            pe.button.rect((275, 200, 50, 50), pe.colors.gray, pe.colors.darkgray, bt['+'], set_lerplength,
                           lerplength + .1)
            mp = pe.mouse.pos()
            lerp1 = pe.math.lerp((0, 0), mp, lerplength)
            lerp2 = pe.math.lerp((pe.display.get_width(), 0), mp, lerplength)
            lerp3 = pe.math.lerp((0, pe.display.get_height()), mp, lerplength)
            lerp4 = pe.math.lerp(pe.display.get_size(), mp, lerplength)

            lerp1max = pe.math.lerp((0, 0), mp, min(1, lerplength))
            # noinspection PyTypeChecker
            lerp2max = pe.math.lerp((pe.display.get_width(), 0), mp, min(1, lerplength))
            # noinspection PyTypeChecker
            lerp3max = pe.math.lerp((0, pe.display.get_height()), mp, min(1, lerplength))
            # noinspection PyTypeChecker
            lerp4max = pe.math.lerp(pe.display.get_size(), mp, min(1, lerplength))

            pe.draw.line(pe.colors.red, (0, 0), mp, 2)
            pe.draw.line(pe.colors.red, (pe.display.get_width(), 0), mp, 2)
            pe.draw.line(pe.colors.red, (0, pe.display.get_height()), mp, 2)
            pe.draw.line(pe.colors.red, (pe.display.get_width(), pe.display.get_height()), mp, 2)

            pe.draw.line(pe.colors.pink, (0, 0), lerp1, 3)
            pe.draw.line(pe.colors.pink, (pe.display.get_width(), 0), lerp2, 3)
            pe.draw.line(pe.colors.pink, (0, pe.display.get_height()), lerp3, 3)
            pe.draw.line(pe.colors.pink, (pe.display.get_width(), pe.display.get_height()), lerp4, 3)

            pe.draw.line(pe.colors.white, (0, 0), lerp1max, 5)
            pe.draw.line(pe.colors.white, (pe.display.get_width(), 0), lerp2max, 5)
            pe.draw.line(pe.colors.white, (0, pe.display.get_height()), lerp3max, 5)
            pe.draw.line(pe.colors.white, (pe.display.get_width(), pe.display.get_height()), lerp4max, 5)
        elif test == "math_center":
            pe.draw.circle(pe.colors.white, pe.math.center((0, 0, pe.display.get_width(), pe.display.get_height())), 5,
                           5)
        elif test == "math_dist":
            pe.draw.line(pe.colors.red, (0, 0), pe.mouse.pos(), 2)
            bt['distance'].text = f'{pe.math.dist((0, 0), pe.mouse.pos()):.3f}'
            bt['distance'].init()
            bt['distance'].display()
        elif test == "math_tsx":
            pe.button.rect((100, 145, 50, 50), pe.colors.gray, pe.colors.darkgray, bt['-'], set_tsx_radius,
                           tsx.radius - .3)
            pe.button.rect((100, 200, 50, 50), pe.colors.gray, pe.colors.darkgray, bt['-'], set_tsx_segments,
                           max(2, tsx_segments - .1))
            pe.button.rect((100, 255, 50, 50), pe.colors.gray, pe.colors.darkgray, bt['-'], set_tsx_offset,
                           tsx.offset - 1)
            bt['tsx_radius'].text = f'radius {tsx.radius:.1f}'
            bt['tsx_radius'].init()
            bt['tsx_radius'].display()
            bt['tsx_segments'].text = f'segments {int(tsx_segments)}'
            bt['tsx_segments'].init()
            bt['tsx_segments'].display()
            bt['tsx_offset'].text = f'rotation offset {tsx.offset:.1f}'
            bt['tsx_offset'].init()
            bt['tsx_offset'].display()
            pe.button.rect((350, 145, 50, 50), pe.colors.gray, pe.colors.darkgray, bt['+'], set_tsx_radius,
                           tsx.radius + .3)
            pe.button.rect((350, 200, 50, 50), pe.colors.gray, pe.colors.darkgray, bt['+'], set_tsx_segments,
                           min(360, tsx_segments + .1))
            pe.button.rect((350, 255, 50, 50), pe.colors.gray, pe.colors.darkgray, bt['+'], set_tsx_offset,
                           tsx.offset + 1)
            gen = (tsx[rotation] for rotation in range(0, 360, max(360 // int(tsx_segments), 1)))
            pe.draw.polygon(pe.colors.red, list(gen), 2)
        log.render()
        pe.display.update(120)
        pe.stop_recording()
        if pe.mouse.clicked()[2]:
            pe.start_debug()


if __name__ == '__main__':
    run()
