import os
import pygameextra as pe
from pygameextra.debug import FreeInteractMode

pe.init()
pe.display.make((500, 500), "PGE Testing Utility", 0)
sp = os.path.dirname(os.path.realpath(__file__))

# Button images
bX = pe.Image(f"{sp}/Xbutton.png", size=(100, 100), position=(100, 0))
bX2 = pe.Image(f"{sp}/Xbutton.png", size=(10, 10), position=(100, 0))
sX = pe.Image(f"{sp}/Xbutton.png", size=(20, 20), position=(100, 0))
bY = pe.Image(f"{sp}/Ybutton.png", size=(100, 100), position=(100, 0))
bY2 = pe.Image(f"{sp}/Ybutton.png", size=(10, 10), position=(100, 0))

s1 = pe.Sprite(pe.Sheet(f"{sp}/rows.png", pe.SHEET_VERTICAL(16, 16)), (250, 250), (0, 0), pivot="topleft")  # Rows sprite
s2 = pe.Sprite(pe.Sheet(f"{sp}/columns.png", pe.SHEET_HORIZONTAL(32, 32)), (250, 250), (250, 0), pivot="topleft")  # Columns sprite

# Resized sprites
s3 = pe.Sprite(f"{sp}/mario_01.png", (250, 250), pe.math.center((0, 250, 125, 125)))  # Resized sprite 1
s3.size = 0.5

s4 = pe.Sprite(f"{sp}/mario_01.png", (250, 250), pe.math.center((125, 250, 125, 125)))  # Resized sprite 2
s4.size = 0.25

s5 = pe.Sprite(f"{sp}/mario_01.png", (250, 250), pe.math.center((0, 375, 125, 125)))  # Resized sprite 3
s5.size = 0.1

s6 = pe.Sprite(f"{sp}/mario_01.png", (250, 250), pe.math.center((125, 375, 125, 125)))  # Resized sprite 4
s6.size = 0.05

s7 = pe.Sprite(f"{sp}/mario_01.png", (250, 250), pe.math.center((250, 250, 250, 250)), 90, pivot="center")  # Rotated sprite

# Init sprites
# s1.init()
# s2.init()
# s3.init()
# s4.init()
# s5.init()
# s6.init()
# s7.init()

# Setup some more things...
bt = [  # Button texts
    pe.text.quick('Buttons', 15, pe.math.center((0, 200, 100, 50))),
    pe.text.quick('Sliders', 15, pe.math.center((100, 200, 100, 50))),
    pe.text.quick('< Back', 15, pe.math.center((0, 0, 100, 50))),
    pe.text.quick('Sprites', 15, pe.math.center((200, 200, 100, 50))),
    pe.text.quick('Shapes', 15, pe.math.center((300, 200, 100, 50))),
    pe.text.quick('Math', 15, pe.math.center((400, 200, 100, 50))),
    pe.text.quick('Lerp', 15, pe.math.center((0, 200, 100, 50))),
    pe.text.quick('Center', 15, pe.math.center((100, 200, 100, 50))),
    pe.text.quick('< Math', 15, pe.math.center((0, 0, 100, 50))),
    pe.text.quick('+', 15, pe.math.center((275, 200, 50, 50))),
    pe.text.quick('-', 15, pe.math.center((175, 200, 50, 50))),
    pe.text.quick("100", 15, pe.math.center((225, 200, 50, 50)))
]
bt[8].color = pe.colors.white
bt[8].init()
bt[11].color = pe.colors.white
bt[11].init()
s1.step = 0.1  # Set sprite animation
s2.step = 0.1  # Set sprite animation
s2.pingpong = True  # Enable sprite pong
sO = 50  # Set slider variable
sT = 50  # Set slider variable
test = ""
testall = 0
testdrop = -100
lerplength = 100


# Button function
def set_test(data):
    global test
    test = data
    if "math_" in data:
        pe.display.make((500, 500), "PGE Testing Utility", 1)
    else:
        pe.display.make((500, 500), "PGE Testing Utility", 0)


def set_lerplength(data):
    global lerplength
    lerplength = data


# Test functions
testscore = 0

pe.settings.debugger = FreeInteractMode()

# Main GAME LOOP
def run():
    while True:
        for pe.event.c in pe.event.get():
            pe.event.quitcheckauto()
        pe.start_recording()
        pe.fill.full(pe.colors.verydarkgray)

        if test == "slider":
            sO = pe.slider.boxed((125, 100, 250, 15, 20), (255, 0, 0), 0, 100, sO, (0, 0, 255), (0, 0, 0), (0, 255, 0), True, (0, 0, 255))
            sT = pe.slider.normal((125, 150, 250, 15, 20), sX.old, 0, 100, sT, (255, 255, 255), (0, 255, 0), 5, True, (0, 0, 255), 3)
        elif test == "button":
            x = 0
            y = 0
            while x < 49 and y < 49:
                # bX2.position = (x+150, y+200)
                # bX2.rect = bX2.object.get_rect(topleft=(x+150, y+200))
                # bY2.position = (x + 150, y + 200)
                # bY2.rect = bY2.object.get_rect(topleft=(x + 150, y + 200))
                pe.button.rect((x+100, y+200, 10, 10), pe.colors.red, pe.colors.green)
                pe.button.image((x+150, y+200, 10, 10), bX2, bY2)
                x += 10
                if x > 49:
                    x = 0
                    y += 10
        elif test == "sprite":
            s1.display()
            s2.display()
            s3.display()
            s4.display()
            s5.display()
            s6.display()
            s7.display()
        elif test == "shapes":
            pe.draw.circle(pe.colors.red, (125, 125), 50, 5)
            pe.draw.circle(pe.colors.aqua, (125, 125), 40, 0)
            pe.draw.rect(pe.colors.red, (325, 75, 100, 100), 5)
            pe.draw.rect(pe.colors.aqua, (335, 85, 80, 80), 0)
            pe.draw.line(pe.colors.red, (0, 250), (250, 500), 5)
            pe.draw.line(pe.colors.red, (250, 250), (0, 500), 5)
            pe.draw.ellipse(pe.colors.red, (250, 250, 250, 250))

        if test == "":
            pe.button.rect((0, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt[0], action=set_test, data="button")
            pe.button.rect((100, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt[1], action=set_test, data="slider", disabled=pe.colors.gray)
            pe.button.rect((200, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt[3], action=set_test, data="sprite", disabled=pe.colors.gray)
            pe.button.rect((300, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt[4], action=set_test, data="shapes")
            pe.button.rect((400, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt[5], action=set_test, data="math")
        elif test == "math":
            pe.button.rect((0, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt[6], action=set_test, data="math_lerp")
            pe.button.rect((100, 200, 100, 50), pe.colors.white, pe.colors.lightgray, bt[7], action=set_test, data="math_center")
        if test != "":
            if "math_" in test:
                pe.button.rect((0, 0, 100, 50), pe.colors.verydarkgray, pe.colors.darkgray, bt[8], action=set_test, data="math")
            elif test == "testall":
                pass
            else:
                pe.button.rect((0, 0, 100, 50), pe.colors.white, pe.colors.lightgray, bt[2], action=set_test, data="")
            #

        if test == "math_lerp":
            if pe.display.get_width() < 325 or pe.display.get_height() < 250:
                x, y = 0, 0
                s = pe.display.get_size()
                while s[0]+x < 325 or s[1]+y < 250:
                    if s[0]+x < 325:
                        x += 1
                    if s[1]+y < 250:
                        y += 1
                pe.display.make((s[0]+x, s[1]+y), "PGE Testing Utility", 1)
            pe.button.rect((175, 200, 50, 50), pe.colors.gray, pe.colors.darkgray, bt[10], set_lerplength, lerplength-10)
            bt[11].text = str(lerplength)
            bt[11].init()
            bt[11].display()
            pe.button.rect((275, 200, 50, 50), pe.colors.gray, pe.colors.darkgray, bt[9], set_lerplength, lerplength+10)
            mp = pe.mouse.pos()
            lerp1 = pe.math.lerp((0, 0), mp, lerplength)
            lerp2 = pe.math.lerp((pe.display.get_width(), 0), mp, lerplength)
            lerp3 = pe.math.lerp((0, pe.display.get_height()), mp, lerplength)
            lerp4 = pe.math.lerp(pe.display.get_size(), mp, lerplength)

            pe.draw.line(pe.colors.red, (0, 0), mp, 5)
            pe.draw.line(pe.colors.red, (pe.display.get_width(), 0), mp, 5)
            pe.draw.line(pe.colors.red, (0, pe.display.get_height()), mp, 5)
            pe.draw.line(pe.colors.red, (pe.display.get_width(), pe.display.get_height()), mp, 5)

            pe.draw.line(pe.colors.white, (0, 0), lerp1, 5)
            pe.draw.line(pe.colors.white, (pe.display.get_width(), 0), lerp2, 5)
            pe.draw.line(pe.colors.white, (0, pe.display.get_height()), lerp3, 5)
            pe.draw.line(pe.colors.white, (pe.display.get_width(), pe.display.get_height()), lerp4, 5)
        elif test == "math_center":
            pe.draw.circle(pe.colors.white, pe.math.center((0, 0, pe.display.get_width(), pe.display.get_height())), 5, 5)
        pe.display.update(120)
        pe.stop_recording()
        if pe.mouse.clicked()[1]:
            pe.start_debug()


if __name__ == '__main__':
    run()