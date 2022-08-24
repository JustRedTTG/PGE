import pygameextra as pe

pe.init()

pe.display.make((250, 250), "Cool", pe.display.DISPLAY_MODE_RESIZABLE)


while True:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    #pe.fill.interlace((50, 50, 50), 2)
    pe.fill.interlace((255, 50, 50), 5)
    pe.display.update()
