import pygameextra as pe
from random import randint
size = (1000, 500)
pe.init(size)

sprite = pe.Sprite('image.jpg', size)

pe.display.make(size) # Init display
cubes = []
x,y=0,0
cell = int(size[0]/200)
while y <= size[1]:
    while x <= size[0] * 2:
        cubes.append([x, y, x, y])
        x += cell
    x = 0
    y += cell
while True:
    for pe.event.c in pe.event.get(): pe.event.quitcheckauto()

    for cube in cubes:
        sprite.display(position=(cube[2], cube[3]), area=(cube[0], cube[1], cell, cell))
    for _ in range(1000):
        i = randint(0, len(cubes)-1)
        new_pos = (cubes[i][0] + (randint(0,2)-1) * cell, cubes[i][1] + (randint(0,2)-1) * cell)
        new_pos = (
            max(0, min(size[0]-cell, new_pos[0])),
            max(0, min(size[1]-cell, new_pos[1]))
        )
        i2 = 0
        while i2 < len(cubes):
            if (cubes[i2][0], cubes[i2][1]) == new_pos:
                cubes[i2][0] = cubes[i][0]
                cubes[i2][1] = cubes[i][1]
                break
            i2 += 1
        cubes[i][0] = new_pos[0]
        cubes[i][1] = new_pos[1]
    pe.display.update()