import pygameextra as pe
from tests.common import PygameExtraTest


class TestSurface(PygameExtraTest):
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
