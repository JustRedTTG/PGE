import time
import unittest
from types import GeneratorType

import pygameextra as pe

SCREEN_FLASH_TIME = 0.01
BETWEEN_FRAME_TIME = 0.001  # Prevents errors, please use, can slow down tests that do multiple frames
SCREEN_FLASH_MAIN = (*pe.colors.verydarkpink, 10)
SCREEN_FLASH_PARENT = (*pe.colors.verydarkblue, 10)
SCREEN_MODE = pe.display.DISPLAY_MODE_NORMAL
TEST_FPS = 0  # 600 -> .1 second when tests are tailored for 60 fps
# USE 0 FOR INFINITE FPS

def between_frame_sleep():
    if BETWEEN_FRAME_TIME:
        time.sleep(BETWEEN_FRAME_TIME)

def screen_flash_sleep():
    if SCREEN_FLASH_TIME:
        time.sleep(SCREEN_FLASH_TIME)


class PygameExtraTest(unittest.TestCase):
    class ContextingLogic:
        def __enter__(self):
            pe.fill.full(pe.colors.black)

        def __exit__(self, exc_type, exc_val, exc_tb):
            pe.draw.circle(pe.colors.yellow, pe.mouse.pos(), 5, 1)
            pe.display.update(TEST_FPS)
            between_frame_sleep()

        @property
        def display_reference(self):
            return pe.display.display_reference

    def setUp(self):
        pe.display.make((500, 500), "tests", SCREEN_MODE)
        self.context = self.ContextingLogic()

    def tearDown(self):
        pe.fill.full(SCREEN_FLASH_MAIN)
        pe.display.update()
        screen_flash_sleep()

    def assert_surfaces_are_same(self, surface1: pe.Surface, surface2: pe.Surface):
        self.assertEqual(surface1.size, surface2.size, "Sizes should be the same")
        for x in range(surface1.size[0]):
            for y in range(surface1.size[1]):
                self.assertEqual(surface1.get_at((x, y)), surface2.get_at((x, y)),
                                 f"Color at {x}, {y} should be the same")

    def _test_sheet_matches(self, sheet: pe.Sheet, generator: GeneratorType):
        for i in generator:
            rect = sheet.handler.get(i)

            color_a = sheet.surface.get_at(rect[:2])[0]
            color_b = sheet.surface.get_at(tuple(pos + size - 1 for pos, size in zip(rect[:2], rect[2:])))[0]

            on_color = 'A'
            try:
                self.assertEqual(color_a, i, "The sheet color A should match the gradient index")
                on_color = 'B'
                self.assertEqual(color_b, i, "The sheet color B should match the gradient index")
            except AssertionError as e:
                surface = pe.Surface(size=rect[2:])
                surface.stamp(sheet.surface, area=rect)
                surface.save_to_file(f"tests/_test_errors/test_sheet_COLOR_{on_color}_{i}_cut.png")
                with sheet.surface:
                    pe.draw.rect(pe.colors.red, rect, 1)
                sheet.surface.save_to_file(f"tests/_test_errors/test_sheet_COLOR_{on_color}_{i}_outlined.png")
                raise e

    def spoof_mouse(self, position: tuple = None):
        pe.settings.spoof_mouse_position = tuple(
            v - o for v, o in zip(position, pe.settings.spoof_mouse_offset or (0, 0)))

    def spoof_click(self, button: int = None):
        if button is None:
            pe.settings.spoof_mouse_clicked = None
            return
        buttons = [False, False, False]
        buttons[button] = True
        pe.settings.spoof_mouse_clicked = buttons


class PygameExtraSubSurfaceTest(PygameExtraTest):
    class ContextingLogic:
        def __init__(self, context: pe.Surface):
            self._context = context

        def __enter__(self):
            pe.fill.full(pe.colors.verydarkgray)
            self._context.last_blit_pos = (100, 100)
            self._context.__enter__()
            pe.fill.full(pe.colors.black)

        def __exit__(self, exc_type, exc_val, exc_tb):
            pe.draw.circle(pe.colors.yellow, pe.mouse.pos(), 5, 1)
            self._context.__exit__(exc_type, exc_val, exc_tb)
            pe.display.blit(self._context, (100, 100))
            pe.display.update(TEST_FPS)
            between_frame_sleep()

        @property
        def display_reference(self):

            return self._context


    def setUp(self):
        pe.display.make((600, 600), "tests", SCREEN_MODE)
        self._context = pe.Surface((500, 500))
        self.context = self.ContextingLogic(self._context)

    def tearDown(self):
        pe.fill.full(SCREEN_FLASH_PARENT)
        with self._context:
            pe.fill.full(SCREEN_FLASH_MAIN)
        pe.display.blit(self._context, (100, 100))
        pe.display.update()
        screen_flash_sleep()

class PygameExtraDebugGameContext(pe.GameContext):
    def post_loop(self):
        for button in self.buttons:
            pe.draw.rect(pe.colors.yellow, (
                *tuple(v + o for v, o in zip(button.area[:2], button.display_reference.last_blit_pos)),
                *button.area[2:]
            ), 1)
        pe.draw.circle(pe.colors.yellow, pe.mouse.pos(), 5, 1)
        super().post_loop()


class PygameExtraContextTest(PygameExtraTest):
    AREA = (500, 500)

    class TestContext(PygameExtraDebugGameContext):
        BACKGROUND = pe.colors.black
        FPS = TEST_FPS
        MODE = SCREEN_MODE

        def __init__(self, area):
            self.AREA = area
            super().__init__()

        def loop(self):
            pass

    class ContextingLogic:
        def __enter__(self):
            pe.settings.game_context.__enter__()

        def __exit__(self, exc_type, exc_val, exc_tb):
            pe.settings.game_context.__exit__(exc_type, exc_val, exc_tb)
            between_frame_sleep()

        @property
        def display_reference(self):
            return pe.display.display_reference

    def setUp(self):
        self._context = self.TestContext(self.AREA)
        self.context = self.ContextingLogic()

    def tearDown(self):
        with self._context:
            pe.fill.full(SCREEN_FLASH_MAIN)
        screen_flash_sleep()
        super().tearDown()
        pe.settings.game_context = None


class PygameExtraSubContextTest(PygameExtraTest):
    AREA = (500, 500)

    class TestContext(PygameExtraDebugGameContext):
        BACKGROUND = pe.colors.verydarkgray
        FPS = TEST_FPS
        MODE = SCREEN_MODE

        class TestSubContext(pe.Context):
            BACKGROUND = pe.colors.black

            def __init__(self, area):
                self.AREA = area
                super().__init__()

            def loop(self):
                pass

            def post_loop(self):
                pe.draw.circle(pe.colors.aqua, pe.mouse.pos(), 7, 3)

        def __init__(self, area):
            self.AREA = tuple(s * 2 for s in area)
            self.sub_context = self.TestSubContext(area)
            super().__init__()

        def loop(self):
            pass

    class ContextingLogic:
        def __enter__(self):
            pe.settings.game_context.__enter__()
            pe.settings.game_context.sub_context.__enter__()

        def __exit__(self, exc_type, exc_val, exc_tb):
            pe.settings.game_context.sub_context.__exit__(exc_type, exc_val, exc_tb)
            pe.settings.game_context.__exit__(exc_type, exc_val, exc_tb)
            between_frame_sleep()

        @property
        def display_reference(self):
            return pe.settings.game_context.sub_context.surface

    def setUp(self):
        self._context = self.TestContext(self.AREA)
        self.context = self.ContextingLogic()

    def tearDown(self):
        with self._context:
            pe.fill.full(SCREEN_FLASH_PARENT)
            with self._context.sub_context:
                pe.fill.full(SCREEN_FLASH_MAIN)
        screen_flash_sleep()
        super().tearDown()
        pe.settings.game_context = None
