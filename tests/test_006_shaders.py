import time
from random import randint

import pygameextra as pe

from tests.common import PygameExtraTest, PygameExtraContextTest, PygameExtraSubContextTest, PygameExtraSubSurfaceTest, \
    PygameExtraWithButtonManagerTest, PygameExtraSubSurfaceWithButtonManagerTest, PygameExtraContextTestShader


class ShaderInitTest(PygameExtraContextTestShader):
    AREA = (200, 200)
    FRAMES_TO_SIMULATE = 60  # One full second

    context: pe.ShaderGameContext

    def setUp(self):
        super().setUp()

    def check_color_using_texture(self, color, x_y: tuple = (0, 0)):
        self.context.update()
        surface = self.context.surface._default_shader.screen_texture.as_surface()
        self.assertEqual(color, surface.get_at(x_y))

    def test_001_background(self):
        pe.fill.full(pe.colors.red)
        self.check_color_using_texture(pe.colors.red)

    def test_002_transparency(self):
        pe.fill.transparency(pe.colors.red, 128)
        self.check_color_using_texture(pe.colors.red + (128,))

    def test_003_blitting(self):
        pe.draw.rect((*pe.colors.red, 128), (0, 0, 100, 100))
        self.check_color_using_texture(pe.colors.red)


    def test_004_color_invert_shader(self):
        pe.fill.full(pe.colors.red)
        self.check_color_using_texture(pe.colors.aqua)