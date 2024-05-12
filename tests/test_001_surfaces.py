import pygameextra as pe
from tests.common import PygameExtraTest


class TestSurfaceInitialization(PygameExtraTest):
    def test_001_file(self):
        pe.get_surface_file("tests/files/test_png.png")

    def test_002_surface(self):
        surface = pe.get_surface_file(pe.Surface((10, 10)))
        surface.set_at((5, 5), (255, 0, 0))
        self.assertEqual(surface.size, (10, 10), "Size should be 10x10")
        self.assertEqual(surface.get_at((5, 5)), (255, 0, 0), "Color should be (255, 0, 0)")

    def test_003_compressing_surface(self):
        surface = pe.get_surface_file(pe.Surface((10, 10)))
        compressed = surface.compress()
        as_dict = compressed.to_dict()
        pe.CompressedSurface.from_dict(as_dict)

    def test_004_load_compressed_surface(self):
        surface = pe.get_surface_file(pe.Surface((10, 10)))
        surface.set_at((5, 5), (255, 0, 0))
        compressed = pe.CompressedSurface(surface)
        decompressed = compressed.decompress()
        self.assertEqual(decompressed.get_at((5, 5)), (255, 0, 0), "Color should be (255, 0, 0)")

    def test_005_save_surface(self):
        surface = pe.get_surface_file(pe.Surface((10, 10)))
        surface.set_at((5, 5), (255, 0, 0))
        surface.save_to_file("tests/_test_temp/test_save_surface.png")


class TestSurfaceUsage(PygameExtraTest):
    def setUp(self):
        super().setUp()
        self.surface = pe.get_surface_file(pe.Surface((10, 10)))
        with self.surface:
            pe.fill.full(pe.colors.red)

    def test_001_surface_copy(self):
        copy = self.surface.copy()
        self.assert_surfaces_are_same(self.surface, copy)

    def test_002_surface_get_at(self):
        self.assertEqual(self.surface.get_at((5, 5))[:3], pe.colors.red, "Color should be red")

    def test_003_surface_set_at(self):
        self.surface.set_at((5, 5), pe.colors.blue)
        self.assertEqual(self.surface.get_at((5, 5))[:3], pe.colors.blue, "Color should be blue")

    def test_004_surface_blit(self):
        surface = pe.Surface((10, 10))
        surface.stamp(self.surface, (0, 0))
        self.assert_surfaces_are_same(self.surface, surface)

    def test_005_surface_set_alpha(self):
        self.surface.set_alpha(128)
        surface = pe.Surface((10, 10))
        surface.stamp(self.surface, (0, 0))
        self.assertEqual(surface.get_at((5, 5))[3], 128, "Alpha should be 128")

    def test_006_surface_get_info(self):
        self.assertEqual(self.surface.rect.size, (10, 10), "Size should be 10x10")
        self.assertEqual(self.surface.width, 10, "Width should be 10")
        self.assertEqual(self.surface.height, 10, "Height should be 10")

