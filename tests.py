import pygameextra as pe

size = (250, 250)
pe.init(size)

image = pe.Image('image.png', size)

pe.display.make(size) # Init display
while True:
    for pe.event.c in pe.event.get(): pe.event.quitcheckauto()

    image.display()
    pe.display.update()