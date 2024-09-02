from random import randint

import pygameextra as pe

from tests.common import PygameExtraTest, PygameExtraContextTest, PygameExtraSubContextTest, PygameExtraSubSurfaceTest, \
    PygameExtraWithButtonManagerTest, PygameExtraSubSurfaceWithButtonManagerTest


class AbstractButtonTest(PygameExtraTest):
    AREA = (200, 200)
    context: pe.Context
    EXPECT_OVERLAYING = True
    FRAMES_TO_SIMULATE = 60  # One full second

    def setUp(self):
        super().setUp()
        self.ignore_first_frame = self.FRAMES_TO_SIMULATE > 1
        self.do_jumble = self.FRAMES_TO_SIMULATE > 1
        self.area = (0, 0, 100, 100)
        self.area2 = (50, 0, 100, 100)
        self.color_inactive = pe.colors.red
        self.color_active = pe.colors.green
        pe.settings.spoof_mouse_position = None
        pe.settings.spoof_mouse_offset = None
        pe.settings.button_lock = None
        pe.settings.raise_error_for_button_without_name = True

    def jumble(self):
        if not self.do_jumble:
            return
        rect = pe.Rect(*self.area2)
        start = rect.right
        for i in range(10):
            for j in range(randint(1, 20), randint(1, 50)):
                pe.button.rect((start + j, i * 5, 1, 5), pe.colors.verydarkred, pe.colors.verydarkred,
                               name=f"jumble_{i}_{j}")

    def center_mouse_on_button(self):
        self.spoof_mouse(self.button_center)

    def center_mouse_on_button2(self):
        self.spoof_mouse(self.button_center2)

    def center_mouse_on_mid(self):
        self.spoof_mouse(self.button_center_mid)

    @property
    def button_center(self):
        pos = pe.math.center(self.area)
        return (pos[0] - 10, pos[1] - 10)

    @property
    def button_center2(self):
        pos = pe.math.center(self.area2)
        return (pos[0] + 10, pos[1] + 10)

    @property
    def button_center_mid(self):
        return pe.math.lerp(self.button_center, self.button_center2, .5)

    def check_color(self, position, color, msg, index):
        if self.ignore_first_frame and index < 1:
            return
        self.assertEqual(color, self.context.display_reference.get_at(position)[:3], msg)

    def test_001_button_no_hover(self):
        for _ in range(self.FRAMES_TO_SIMULATE):
            with self.context:
                self.spoof_mouse(tuple(v + 10 for v in self.area[2:]))
                self.jumble()
                pe.button.rect(self.area, self.color_inactive, self.color_active, name="button")
            self.check_color(self.button_center, self.color_inactive, "Button should be inactive", _)

    def test_002_button_with_hover(self):
        for _ in range(self.FRAMES_TO_SIMULATE):
            with self.context:
                self.center_mouse_on_button()
                self.jumble()
                pe.button.rect(self.area, self.color_inactive, self.color_active, name="button")
            self.check_color(self.button_center, self.color_active, "Button should be active", _)

    def test_003_button_no_hover_action(self):
        for _ in range(self.FRAMES_TO_SIMULATE):
            with self.context:
                self.spoof_mouse(tuple(v + 10 for v in self.area[2:]))
                self.jumble()
                pe.button.rect(self.area, self.color_inactive, (0, 0, 0, 0), hover_action=pe.draw.rect,
                               hover_data=(self.color_active, self.area), name="button")
            self.check_color(self.button_center, self.color_inactive, "Button action shouldn't be there", _)

    def test_004_button_with_hover_action(self):
        for _ in range(self.FRAMES_TO_SIMULATE):
            with self.context:
                self.center_mouse_on_button()
                self.jumble()
                pe.button.rect(self.area, self.color_inactive, (0, 0, 0, 0), hover_action=pe.draw.rect,
                               hover_data=(self.color_active, self.area), name="button")
            self.check_color(self.button_center, self.color_active, "Button action should be there", _)

    def test_005_button_overlaying(self):
        for _ in range(self.FRAMES_TO_SIMULATE):
            with self.context:
                self.center_mouse_on_mid()
                self.jumble()
                pe.button.rect(self.area, self.color_inactive, self.color_active, name="button")
                pe.button.rect(self.area2, self.color_inactive, self.color_active, name="button2")
            if self.EXPECT_OVERLAYING:
                self.check_color(self.button_center, self.color_inactive, "Button 1 shouldn't be active", _)
            else:
                self.check_color(self.button_center, self.color_active, "Button 1 should be active", _)
            self.check_color(self.button_center_mid, self.color_active, "Button 2 should be active", _)

    def test_006_button_no_draw_hover(self):
        for _ in range(self.FRAMES_TO_SIMULATE):
            with self.context:
                self.spoof_mouse(tuple(v + 10 for v in self.area[2:]))
                self.jumble()
                pe.button.rect(self.area, self.color_inactive, pe.colors.black, hover_draw_action=pe.draw.rect,
                               hover_draw_data=(self.color_active, self.area), name="button")
            self.check_color(self.button_center, self.color_inactive, "Button draw action shouldn't be visible", _)

    def test_007_button_with_draw_hover(self):
        for _ in range(self.FRAMES_TO_SIMULATE):
            with self.context:
                self.center_mouse_on_button()
                self.jumble()
                pe.button.rect(self.area, self.color_inactive, pe.colors.black, hover_draw_action=pe.draw.rect,
                               hover_draw_data=(self.color_active, self.area), name="button")
            self.check_color(self.button_center, self.color_active, "Button draw action should be visible", _)

    def test_008_button_no_click(self):
        result = {'clicked': False}
        for _ in range(self.FRAMES_TO_SIMULATE):
            with self.context:
                self.spoof_click()
                self.center_mouse_on_button()
                self.jumble()
                pe.button.rect(self.area, self.color_inactive, self.color_active,
                               action=result.update, data={"clicked": True}, name="button")
            self.assertEqual(False, result['clicked'], "Button shouldn't be clicked")

    def test_009_button_click(self):
        result = {'clicked': False}
        pe.settings.button_lock = None
        for _ in range(self.FRAMES_TO_SIMULATE):
            with self.context:
                self.spoof_click(0)
                self.center_mouse_on_button()
                self.jumble()
                pe.button.rect(self.area, self.color_inactive, self.color_active,
                               action=result.update, data={"clicked": True}, name="button")
            self.assertEqual(True, result['clicked'], "Button should be clicked")


class TestButtonsWithoutContext(AbstractButtonTest, PygameExtraTest):
    EXPECT_OVERLAYING = False
    FRAMES_TO_SIMULATE = 1
    pass


class TestButtonsWithSubSurface(AbstractButtonTest, PygameExtraSubSurfaceTest):
    EXPECT_OVERLAYING = False
    FRAMES_TO_SIMULATE = 1
    pass


class TestButtonsWithButtonManager(AbstractButtonTest, PygameExtraWithButtonManagerTest):
    pass


class TestButtonsWithSubSurfaceAndButtonManager(AbstractButtonTest, PygameExtraSubSurfaceWithButtonManagerTest):
    pass


class TestButtonsInContext(AbstractButtonTest, PygameExtraContextTest):
    pass


class TestButtonsInSubContext(AbstractButtonTest, PygameExtraSubContextTest):
    pass


# Disallow usage of the abstract tests
del AbstractButtonTest
