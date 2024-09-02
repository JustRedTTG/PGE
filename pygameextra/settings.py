from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygameextra import context

rundown_enabled = True
auto_fps = True
debugger = None

spoof_mouse_offset = None
spoof_mouse_position = None
spoof_mouse_clicked = None
spoof_enabled = True

button_lock_timeout_time = .1  # The button locking timeout
button_lock = None  # The button locking variable
button_lock_enabled = True  # Enable button locking
button_lock_hold = True  # Holding the button will keep it locked

hover_lock_timeout_time = .1  # The hover locking timeout
hover_lock = None  # The hover locking variable
hover_lock_enabled = False  # Enable hover locking

atlas_attempt_keep_past_attempt = True  # When trying to fit the atlas, keep the past attempt on the new size, may speed up the process

game_context: context.GameContext = None
use_button_context_indexing = True
raise_error_for_button_without_name = False
do_not_render_if_hover_draw = False
