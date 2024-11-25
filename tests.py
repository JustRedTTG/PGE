import os
import time
import pygameextra as pe

from functools import lru_cache

from pygameextra import event

pe.init()

os.makedirs("tests/_test_temp", exist_ok=True)

class Tests(pe.GameContext):
    TITLE = "tests"
    AREA = (700, 700)
    BACKGROUND = pe.colors.verydarkgray
    FPS = 60
    FPS_LOGGER = True
    MODE = pe.display.DISPLAY_MODE_RESIZABLE

    SPRITE_RESIZE = 50

    def __init__(self):
        super().__init__()

        self.input_box = pe.InputBox((10, 10, 200, 32), initial_value="A nice long text, to test things out")

    def loop(self):
        pe.draw.rect(pe.colors.darkgray, self.input_box.area)
        self.input_box.display()


tests = Tests()

while True:
    tests()
