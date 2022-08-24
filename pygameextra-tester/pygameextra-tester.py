import pygameextra as pe
pe.init()
pe.display.make((500, 500), "PGE Testing Utility", 0)
sp = ""

# Button images
bX = pe.Image(sp+"Xbutton.png", size=(100, 100), position=(100, 0))
bX2 = pe.Image(sp+"Xbutton.png", size=(10, 10), position=(100, 0))
sX = pe.Image(sp+"Xbutton.png", size=(20, 20), position=(100, 0))
bY = pe.Image(sp+"Ybutton.png", size=(100, 100), position=(100, 0))
bY2 = pe.Image(sp+"Ybutton.png", size=(10, 10), position=(100, 0))

s1 = pe.Sprite(pe.sheet(sp+"rows.png", (16, 16), pe.sheet.rows), (250, 250), (0, 0), pivot="topleft")  # Rows sprite
s2 = pe.Sprite(pe.sheet(sp+"columns.png", (32, 32), pe.sheet.columns), (250, 250), (250, 0), pivot="topleft")  # Columns sprite

# Resized sprites
s3 = pe.Sprite(sp+"mario_01.png", (250, 250), pe.math.center((0, 250, 125, 125)))  # Resized sprite 1
s3.size = 0.5

s4 = pe.Sprite(sp+"mario_01.png", (250, 250), pe.math.center((125, 250, 125, 125)))  # Resized sprite 2
s4.size = 0.25

s5 = pe.Sprite(sp+"mario_01.png", (250, 250), pe.math.center((0, 375, 125, 125)))  # Resized sprite 3
s5.size = 0.1

s6 = pe.Sprite(sp+"mario_01.png", (250, 250), pe.math.center((125, 375, 125, 125)))  # Resized sprite 4
s6.size = 0.05

s7 = pe.Sprite(sp+"mario_01.png", (250, 250), pe.math.center((250, 250, 250, 250)), 90, pivot="center")  # Rotated sprite

# Init sprites
s1.init()
s2.init()
s3.init()
s4.init()
s5.init()
s6.init()
s7.init()

# Setup some more things...
bt = [  # Button texts
    pe.text.quick.make('Buttons', 15, pe.math.center((0, 200, 100, 50))),
    pe.text.quick.make('Sliders', 15, pe.math.center((100, 200, 100, 50))),
    pe.text.quick.make('< Back', 15, pe.math.center((0, 0, 100, 50))),
    pe.text.quick.make('Sprites', 15, pe.math.center((200, 200, 100, 50))),
    pe.text.quick.make('Shapes', 15, pe.math.center((300, 200, 100, 50))),
    pe.text.quick.make('Math', 15, pe.math.center((400, 200, 100, 50))),
    pe.text.quick.make('Lerp', 15, pe.math.center((0, 200, 100, 50))),
    pe.text.quick.make('Center', 15, pe.math.center((100, 200, 100, 50))),
    pe.text.quick.make('< Math', 15, pe.math.center((0, 0, 100, 50))),
    pe.text.quick.make('+', 15, pe.math.center((275, 200, 50, 50))),
    pe.text.quick.make('-', 15, pe.math.center((175, 200, 50, 50))),
    pe.text.quick.make("100", 15, pe.math.center((225, 200, 50, 50)))
]
bt[8].color = pe.color.white
bt[8].init(bt[8])
bt[11].color = pe.color.white
bt[11].init(bt[11])
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


# Main GAME LOOP
while True:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    pe.fill.full(pe.color.verydarkgray)

    if test == "slider":
        sO = pe.slider.boxed((125, 100, 250, 15, 20), (255, 0, 0), 0, 100, sO, (0, 0, 255), (0, 0, 0), (0, 255, 0), True, (0, 0, 255))
        sT = pe.slider.normal((125, 150, 250, 15, 20), sX.old, 0, 100, sT, (255, 255, 255), (0, 255, 0), 5, True, (0, 0, 255), 3)
    elif test == "button":
        x = 0
        y = 0
        while x < 49 and y < 49:
            bX2.position = (x+150, y+200)
            bX2.rect = bX2.object.get_rect(topleft=(x+150, y+200))
            bY2.position = (x + 150, y + 200)
            bY2.rect = bY2.object.get_rect(topleft=(x + 150, y + 200))
            pe.button.rect((x+100, y+200, 10, 10), pe.color.red, pe.color.green)
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
        pe.draw.circle(pe.color.red, (125, 125), 50, 5)
        pe.draw.circle(pe.color.aqua, (125, 125), 40, 0)
        pe.draw.rect(pe.color.red, (325, 75, 100, 100), 5)
        pe.draw.rect(pe.color.aqua, (335, 85, 80, 80), 0)
        pe.draw.line(pe.color.red, (0, 250), (250, 500), 5)
        pe.draw.line(pe.color.red, (250, 250), (0, 500), 5)
        pe.draw.ellipse(pe.color.red, (250, 250, 250, 250))

    if test == "":
        pe.button.rect((0, 200, 100, 50), pe.color.white, pe.color.lightgray, bt[0], action=set_test, data="button")
        pe.button.rect((100, 200, 100, 50), pe.color.white, pe.color.lightgray, bt[1], action=set_test, data="slider")
        pe.button.rect((200, 200, 100, 50), pe.color.white, pe.color.lightgray, bt[3], action=set_test, data="sprite")
        pe.button.rect((300, 200, 100, 50), pe.color.white, pe.color.lightgray, bt[4], action=set_test, data="shapes")
        pe.button.rect((400, 200, 100, 50), pe.color.white, pe.color.lightgray, bt[5], action=set_test, data="math")
    elif test == "math":
        pe.button.rect((0, 200, 100, 50), pe.color.white, pe.color.lightgray, bt[6], action=set_test, data="math_lerp")
        pe.button.rect((100, 200, 100, 50), pe.color.white, pe.color.lightgray, bt[7], action=set_test, data="math_center")
    if test != "":
        if "math_" in test:
            pe.button.rect((0, 0, 100, 50), pe.color.verydarkgray, pe.color.darkgray, bt[8], action=set_test, data="math")
        elif test == "testall":
            pass
        else:
            pe.button.rect((0, 0, 100, 50), pe.color.white, pe.color.lightgray, bt[2], action=set_test, data="")
        #

    if test == "math_lerp":
        if pe.display.get.size()[0] < 325 or pe.display.get.size()[1] < 250:
            x, y = 0, 0
            s = pe.display.get.size()
            while s[0]+x < 325 or s[1]+y < 250:
                if s[0]+x < 325:
                    x += 1
                if s[1]+y < 250:
                    y += 1
            pe.display.make((s[0]+x, s[1]+y), "PGE Testing Utility", 1)
        pe.button.rect((175, 200, 50, 50), pe.color.gray, pe.color.darkgray, bt[10], set_lerplength, lerplength-10)
        bt[11].text = str(lerplength)
        bt[11].init(bt[11])
        pe.text.display(bt[11])
        pe.button.rect((275, 200, 50, 50), pe.color.gray, pe.color.darkgray, bt[9], set_lerplength, lerplength+10)
        mp = pe.mouse.pos()
        lerp1 = pe.math.lerp((0, 0), mp, lerplength)
        lerp2 = pe.math.lerp((pe.display.get.size()[0], 0), mp, lerplength)
        lerp3 = pe.math.lerp((0, pe.display.get.size()[1]), mp, lerplength)
        lerp4 = pe.math.lerp(pe.display.get.size(), mp, lerplength)

        pe.draw.line(pe.color.red, (0, 0), mp, 5)
        pe.draw.line(pe.color.red, (pe.display.get.size()[0], 0), mp, 5)
        pe.draw.line(pe.color.red, (0, pe.display.get.size()[1]), mp, 5)
        pe.draw.line(pe.color.red, (pe.display.get.size()[0], pe.display.get.size()[1]), mp, 5)

        pe.draw.line(pe.color.white, (0, 0), lerp1, 5)
        pe.draw.line(pe.color.white, (pe.display.get.size()[0], 0), lerp2, 5)
        pe.draw.line(pe.color.white, (0, pe.display.get.size()[1]), lerp3, 5)
        pe.draw.line(pe.color.white, (pe.display.get.size()[0], pe.display.get.size()[1]), lerp4, 5)
    elif test == "math_center":
        pe.draw.circle(pe.color.white, pe.math.center((0, 0, pe.display.get.size()[0], pe.display.get.size()[1])), 5, 5)
    pe.display.update()
    pe.time.tick(200)
