import pygameextra as pe
from tests.common import PygameExtraTest


class TestSheetInitialization(PygameExtraTest):
    def test_001_horizontal(self):
        sheet = pe.Sheet(
            "tests/files/test_sheet_horizontal.png",
            pe.SheetHorizontal(30, 30), 255)

        self._test_sheet_matches(sheet, range(255))

    def test_002_vertical(self):
        sheet = pe.Sheet(
            "tests/files/test_sheet_vertical.png",
            pe.SheetVertical(30, 30), 255)

        self._test_sheet_matches(sheet, range(255))

    def test_003_horizontal_loop(self):
        sheet = pe.Sheet(
            "tests/files/test_sheet_horizontal.png",
            pe.SheetHorizontal(30, 30), 255, loop=True)

        self._test_sheet_matches(sheet, range(255))

    def test_004_vertical_loop(self):
        sheet = pe.Sheet(
            "tests/files/test_sheet_vertical.png",
            pe.SheetVertical(30, 30), 255, loop=True)

        self._test_sheet_matches(sheet, range(255))

    def test_005_horizontal_pong(self):
        sheet = pe.Sheet(
            "tests/files/test_sheet_horizontal.png",
            pe.SheetHorizontal(30, 30), 255, pong=True)

        self._test_sheet_matches(sheet, range(255))

    def test_006_vertical_pong(self):
        sheet = pe.Sheet(
            "tests/files/test_sheet_vertical.png",
            pe.SheetVertical(30, 30), 255, pong=True)

        self._test_sheet_matches(sheet, range(255))

    def test_007_horizontal_loop_pong(self):
        sheet = pe.Sheet(
            "tests/files/test_sheet_horizontal.png",
            pe.SheetHorizontal(30, 30), 255, loop=True, pong=True)

        self._test_sheet_matches(sheet, range(255))

    def test_008_vertical_loop_pong(self):
        sheet = pe.Sheet(
            "tests/files/test_sheet_vertical.png",
            pe.SheetVertical(30, 30), 255, loop=True, pong=True)

        self._test_sheet_matches(sheet, range(255))


class TestUsage(PygameExtraTest):
    def setUp(self):
        super().setUp()

        self.sheet = pe.Sheet("tests/files/test_sheet_horizontal.png", pe.SheetHorizontal(30, 30), 255)
        self.sheet_loop = pe.Sheet("tests/files/test_sheet_horizontal.png", pe.SheetHorizontal(30, 30), 255, loop=True)
        self.sheet_pong = pe.Sheet("tests/files/test_sheet_horizontal.png", pe.SheetHorizontal(30, 30), 255, pong=True)
        self.sheet_loop_pong = pe.Sheet("tests/files/test_sheet_horizontal.png", pe.SheetHorizontal(30, 30), 255,
                                        loop=True,
                                        pong=True)

    def test_001_speed(self):
        self.sheet.speed = 2
        self.assertEqual(self.sheet.speed, 2, "Sheet speed is not set correctly")

        self.sheet_loop.speed = 2
        self.assertEqual(self.sheet_loop.speed, 2, "Looping sheet speed is not set correctly")

        self.sheet_pong.speed = 2
        self.assertEqual(self.sheet_pong.speed, 2, "Pong sheet speed is not set correctly")

        self.sheet_loop_pong.speed = 2
        self.assertEqual(self.sheet_loop_pong.speed, 2, "Looping pong sheet speed is not set correctly")
