import os
import time
from functools import lru_cache

import pygameextra as pe

pe.init()

os.makedirs("tests/_test_temp", exist_ok=True)


class Tests(pe.GameContext):
    TITLE = "tests"
    AREA = (500, 500)
    BACKGROUND = pe.colors.verydarkgray
    FPS = 60
    FPS_LOGGER = True
    MODE = pe.display.DISPLAY_MODE_RESIZABLE

    SPRITE_RESIZE = 50

    def __init__(self):
        super().__init__()

        self.sheets = [
            pe.Sheet("tests/files/test_atlas_1.png", pe.SheetHorizontal(10, 30), 20, True, True),
            pe.Sheet("tests/files/test_atlas_2.png", pe.SheetVertical(30, 10), 20, False, True),
        ]

        begin = time.time()
        self.atlas = pe.Atlas.from_sheets({i: sheet for i, sheet in enumerate(self.sheets)})
        print("Atlas creation time:", time.time() - begin)

    @lru_cache
    def sprite(self, index, use_atlas):
        if use_atlas:
            sheet = self.atlas[index].configure(pong=True)
        else:
            sheet = self.sheets[index]
        return pe.Sprite(sheet, (self.SPRITE_RESIZE, self.SPRITE_RESIZE))

    def loop(self):
        # pe.display.blit(self.atlas.surface)

        x, y = 0, 0
        for i in range(len(self.sheets)):
            for use_atlas in (False, True):
                sprite = self.sprite(i, use_atlas)
                sprite.display((x, y))
                x += self.SPRITE_RESIZE
                if x > self.width:
                    x = 0
                    y += self.SPRITE_RESIZE




tests = Tests()

while True:
    tests()
