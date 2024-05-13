import pygameextra as pe
from tests.common import PygameExtraTest


class TestRect(PygameExtraTest):
    def test_001_create(self):
        pe.Rect(5, 5, 10, 10)

    def test_002_parameters(self):
        rect = pe.Rect(5, 5, 10, 10)
        self.assertEqual(rect.x, 5, "X should be 5")
        self.assertEqual(rect.y, 5, "Y should be 5")
        self.assertEqual(rect.w, 10, "Width(w) should be 10")
        self.assertEqual(rect.width, 10, "Width should be 10")
        self.assertEqual(rect.h, 10, "Height(h) should be 10")
        self.assertEqual(rect.height, 10, "Height should be 10")

        self.assertEqual(rect.left, 5, "Left should be 5")
        self.assertEqual(rect.right, 15, "Right should be 15")
        self.assertEqual(rect.top, 5, "Top should be 5")
        self.assertEqual(rect.bottom, 15, "Bottom should be 15")

        self.assertEqual(rect.topleft, (5, 5), "Top left should be (5, 5)")
        self.assertEqual(rect.topright, (15, 5), "Top right should be (15, 5)")
        self.assertEqual(rect.bottomleft, (5, 15), "Bottom left should be (5, 15)")
        self.assertEqual(rect.bottomright, (15, 15), "Bottom right should be (15, 15)")

        self.assertEqual(rect.center, (10, 10), "Center should be (10, 10)")

    # def test_003_transforms(self):

