import pygameextra as pe
pe.init()
pe.Settings.UPDATE_AUTO = True
pe.display.make((100, 100), "Test pe.Sprite")
from os import path
scriptpath = str(path.realpath(__file__)).replace("test_sprite.py",'')

def test_file():
    sprite = pe.Sprite(scriptpath+"testing_assets/sprite-file.png", (50, 50), (50, 50), 70, layer=5)
    assert sprite.frames == 1
    assert sprite.frame == 0
    assert sprite.size == 1
    assert sprite.rect == (50, 50)
    assert sprite.sheet_e == False
    assert sprite.rotation == 70 * 2
    assert sprite.position == (50, 50)
    assert sprite.rotationND == 70
    assert sprite.layer == 5
    assert sprite.step == 0
    assert sprite.step_m == 1


def test_multifile():
    sprite = pe.Sprite([scriptpath + "testing_assets/sprite-multifile01.png", scriptpath + "testing_assets/sprite-multifile02.png", scriptpath + "testing_assets/sprite-multifile03.png"], (50, 50), (50, 50), 70, layer=5)
    assert sprite.frames == 3
    assert sprite.frame == 0
    assert sprite.size == 1
    assert sprite.rect == (50, 50)
    assert sprite.sheet_e == False
    assert sprite.rotation == 70 * 2
    assert sprite.position == (50, 50)
    assert sprite.rotationND == 70
    assert sprite.layer == 5
    assert sprite.step == 0
    assert sprite.step_m == 1


def test_image():
    image = pe.image(scriptpath + "testing_assets/sprite-file.png")
    sprite = pe.Sprite(image, (50, 50), (50, 50), 70, layer=5)
    assert sprite.frames == 1
    assert sprite.frame == 0
    assert sprite.size == 1
    assert sprite.rect == (50, 50)
    assert sprite.sheet_e == False
    assert sprite.rotation == 70 * 2
    assert sprite.position == (50, 50)
    assert sprite.rotationND == 70
    assert sprite.layer == 5
    assert sprite.step == 0
    assert sprite.step_m == 1
    assert sprite.image[0] == image


def test_multiimage():
    image1 = pe.image(scriptpath + "testing_assets/sprite-multifile01.png")
    image2 = pe.image(scriptpath + "testing_assets/sprite-multifile02.png")
    image3 = pe.image(scriptpath + "testing_assets/sprite-multifile03.png")
    sprite = pe.Sprite([image1, image2, image3], (50, 50), (50, 50), 70, layer=5)
    assert sprite.frames == 3
    assert sprite.frame == 0
    assert sprite.size == 1
    assert sprite.rect == (50, 50)
    assert sprite.sheet_e == False
    assert sprite.rotation == 70 * 2
    assert sprite.position == (50, 50)
    assert sprite.rotationND == 70
    assert sprite.layer == 5
    assert sprite.step == 0
    assert sprite.step_m == 1
    assert sprite.image[0] == image1
    assert sprite.image[1] == image2
    assert sprite.image[2] == image3


def test_rows():
    sprite = pe.Sprite(pe.sheet(scriptpath+"testing_assets/sprite-rows.png", (16, 16),pe.sheet.rows), (50, 50), (50, 50), 70, layer=5)
    assert sprite.frames == 12
    assert sprite.frame == 0
    assert sprite.size == 1
    assert sprite.rect == (50, 50)
    assert sprite.sheet.type == pe.sheet.rows
    assert sprite.sheet_e == True
    assert sprite.rotation == 70 * 2
    assert sprite.position == (50, 50)
    assert sprite.rotationND == 70
    assert sprite.layer == 5
    assert sprite.step == 0
    assert sprite.step_m == 1


def test_column():
    sprite = pe.Sprite(pe.sheet(scriptpath+"testing_assets/sprite-rows.png", (16, 16),pe.sheet.columns), (50, 50), (50, 50), 70, layer=5)
    assert sprite.frames == 12
    assert sprite.frame == 0
    assert sprite.size == 1
    assert sprite.rect == (50, 50)
    assert sprite.sheet.type == pe.sheet.columns
    assert sprite.sheet_e == True
    assert sprite.rotation == 70 * 2
    assert sprite.position == (50, 50)
    assert sprite.rotationND == 70
    assert sprite.layer == 5
    assert sprite.step == 0
    assert sprite.step_m == 1