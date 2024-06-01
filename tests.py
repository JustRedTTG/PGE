import os
import time
import pygameextra as pe

from functools import lru_cache

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

        self.loading_screen = pe.animations.PgeIntro(self, False)

    def loop(self):
        pass

    def start_loop(self):
        super().start_loop()
        self.loading_screen()


tests = Tests()

while True:
    tests()
