import pygameextra as pe

from tests.common import PygameExtraTest, PygameExtraContextTest, PygameExtraSubContextTest


class AbstractButtonTest(PygameExtraTest):
    AREA = (200, 200)
    context: pe.Context

    def setUp(self):
        super().setUp()
        self.area = (0, 0, 100, 100)
        self.area2 = (50, 0, 100, 100)
        self.color_inactive = pe.colors.red
        self.color_active = pe.colors.green

    def center_mouse_on_button(self):
        self.spoof_mouse(self.button_center)

    def center_mouse_on_button2(self):
        self.spoof_mouse(self.button_center2)

    def center_mouse_on_mid(self):
        self.spoof_mouse(self.button_center_mid)

    @property
    def button_center(self):
        return pe.math.center(self.area)

    @property
    def button_center2(self):
        return pe.math.center(self.area2)

    @property
    def button_center_mid(self):
        return pe.math.lerp(self.button_center, self.button_center2, .5)

    def check_color(self, position, color, msg):
        self.assertEqual(self.context.display_reference.get_at(position)[:3], color, msg)

    def test_001_button_no_hover(self):
        with self.context:
            self.spoof_mouse(tuple(v + 10 for v in self.area[2:]))
            pe.button.rect(self.area, self.color_inactive, self.color_active)
        self.check_color(self.button_center, self.color_inactive, "Button should be inactive")

    def test_002_button_with_hover(self):
        with self.context:
            self.center_mouse_on_button()
            pe.button.rect(self.area, self.color_inactive, self.color_active)
        self.check_color(self.button_center, self.color_active, "Button should be active")

    def test_003_button_with_hover_action(self):
        with self.context:
            self.center_mouse_on_button()
            pe.button.rect(self.area, self.color_inactive, (0, 0, 0, 0), hover_action=pe.draw.rect,
                           hover_data=(self.color_active, self.area))
        self.check_color(self.button_center, self.color_active, "Button should be active")

    def test_004_button_overlaying(self):
        with self.context:
            self.center_mouse_on_mid()
            pe.button.rect(self.area, self.color_inactive, self.color_active)
            pe.button.rect(self.area2, self.color_inactive, self.color_active)
        self.check_color(self.button_center, self.color_inactive, "Button 1 shouldn't be active")
        self.check_color(self.button_center_mid, self.color_active, "Button 2 should be active")


class TestButtons(AbstractButtonTest, PygameExtraContextTest):
    pass


class TestButtonsInSubContext(AbstractButtonTest, PygameExtraSubContextTest):
    pass


# Disallow usage of the abstract tests
del AbstractButtonTest
