import time

from pygameextra.assets import ASSET_LOADING_ICON, ASSET_FONT
from pygameextra.atlas import Atlas, AtlasFile
from pygameextra.sprite import Sprite
from pygameextra.context import Context, ChildContext, UnclippedContext
from pygameextra.layer_methods import AFTER_POST_LAYER
from pygameextra.rect import Rect
import pygameextra as pe


def get_loading_atlas():
    return Atlas.load_store(ASSET_LOADING_ICON)


class PgeIntro(ChildContext):
    BACKGROUND = None

    def __init__(self, parent, load_on_complete: bool = False):
        display_rect = Rect(0, 0, *pe.display.get_size())
        center = display_rect.center
        display_rect.scale_by_ip(.4, .4)
        display_rect.height = display_rect.width // 2
        display_rect.center = center
        self.load_on_complete = load_on_complete
        self.position = display_rect.topleft
        self.begin_completed = False
        self.wait_begin = None
        center_rect = display_rect.copy()
        super().__init__(parent)
        # self.surface.surface.set_alpha(0)

        self.sprite = Sprite(get_loading_atlas()['pge_icon'], display_rect.size)
        self.loading_trail = None

    def loop(self):
        if pe.settings.game_context.delta_time == 1:
            return
        self.sprite.display(self.position)

        if self.load_on_complete and self.completed:
            pass

    def pre_loop(self):
        super().pre_loop()
        if not (begin_completed := self.completed) or self.load_on_complete:
            self.begin_completed = begin_completed
            pe.fill.full(pe.colors.black)

    def post_loop(self):
        super().post_loop()
        if self.completed and not self.begin_completed and self.wait_begin is None:
            if not self.load_on_complete:
                self.wait_begin = time.time() + 2
        if pe.settings.game_context.fps_logger is not None:
            pe.settings.game_context.FPS_LOGGER = self.completed and not self.load_on_complete

    @property
    def completed(self):
        return self.sprite.index >= self.sprite.reference.frames - 1 and (
                self.wait_begin is None or time.time() >= self.wait_begin)
