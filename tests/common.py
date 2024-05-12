import unittest
from types import GeneratorType

import pygameextra as pe


class PygameExtraTest(unittest.TestCase):
    def setUp(self):
        pe.display.make((500, 500), "tests", pe.display.DISPLAY_MODE_HIDDEN)

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


