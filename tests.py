import os
import random
import time
import pygameextra as pe

from functools import lru_cache

from pygameextra import event

pe.init()

os.makedirs("tests/_test_temp", exist_ok=True)

pe.settings.raise_error_for_button_without_name = True
pe.settings.use_button_context_indexing = False


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

        self.input_box = pe.InputBox(
            (10, 10, self.width - 20, 32),
            initial_value="A nice long text, to test things out",
            text_colors=[pe.colors.white, None]
        )
        self.input_box.focus()

        self.draggable = pe.Draggable((250, 250), area=(100, 100), button_index=2)

    def loop(self):
        pe.draw.rect(pe.colors.darkgray, self.input_box.area)

        for i in range(random.randint(100, 700)):
            pe.button.rect((i*1, 100, 1, 1), pe.colors.red, pe.colors.aqua, name=f"random_button_{i}",
                           hover_draw_action=pe.draw.rect, hover_draw_data=(pe.colors.aqua, (i*1, 100, 1, 100)))

        for i in range(5):
            pe.button.rect((i*50, 120+i*2, 100, 50), pe.colors.red, pe.colors.aqua, name=f"button_{i}")

        self.input_box.display()

        _, pos = self.draggable.check()
        pe.draw.rect(pe.colors.red, (*pos, 100, 100), 2)


tests = Tests()

while True:
    tests()
