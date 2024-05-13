import pygameextra as pe
from tests.common import PygameExtraTest


class TestSheet(PygameExtraTest):
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
