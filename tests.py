from functools import lru_cache

import pygameextra as pe

pe.init()


class Tests(pe.GameContext):
    TITLE = "tests"
    AREA = (500, 500)
    BACKGROUND = pe.colors.verydarkgray
    FPS = 60
    FPS_LOGGER = True

    SPRITE_RESIZE = 100

    def __init__(self):
        super().__init__()

        self.sheets = [
            pe.Sheet("tests/files/test_sheet_horizontal.png", pe.SheetHorizontal(30, 30), 255, True, True),
            pe.Sheet("tests/files/test_sheet_vertical.png", pe.SheetVertical(30, 30), 255, True, True),
        ]

        self.atlas = pe.Atlas.from_sheets({i: sheet for i, sheet in enumerate(self.sheets)})
        exit()

    @lru_cache
    def sprite(self, index, use_atlas):
        if use_atlas:
            return self.atlas[index]
        return pe.Sprite(self.sheets[index], (self.SPRITE_RESIZE, self.SPRITE_RESIZE))

    def loop(self):
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
