import pygameextra as pe
from tests.common import PygameExtraTest


class TestAtlas(PygameExtraTest):
    def setUp(self):
        super().setUp()
        self.test_sheet = pe.get_surface_file("tests/files/test_sheet.png")
