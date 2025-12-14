import pygameextra as pe
from tests.common import PygameExtraTest


class TestAtlas(PygameExtraTest):
    def setUp(self):
        super().setUp()
        self.test_sheet = pe.get_surface_file("tests/files/test_atlas_packing.png")

    def test_001_atlas_packing(self):
        atlas = pe.Atlas.from_sheets({
            'test': pe.Sheet(self.test_sheet, pe.SheetVertical(4, 4))
        })

        self.assertEqual(atlas.surface.size, (8, 8), "Atlas size is incorrect")
        self.assertEqual(atlas.surface.get_at((7, 7)), (255, 255, 255, 50), "Bottom-right pixel is incorrect")
        self.assertEqual(atlas.surface.get_at((0, 0)), (255, 0, 0, 50), "Top-left pixel is incorrect")
