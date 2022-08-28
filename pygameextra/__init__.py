"""PYGAME EXTRA __INIT__"""

import os
# noinspection PyUnresolvedReferences
from pygameextra.pygame import pygame
from pygameextra.image import *
from pygameextra.sheet_handlers import *
from pygameextra.sprite import *
from pygameextra.modified import *
from pygameextra.version import get as get_version
from pygameextra import event, time, fill, mouse, settings, colors, draw, math, text, button, rect

__version__ = get_version()


def init(display_init_size: tuple = None):
    pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
    pygame.init()
    time.init()
    if display_init_size:
        display.make(display_init_size, mode=display.DISPLAY_MODE_HIDDEN)


def start_debug(delete_after: bool = False, reactivate: bool = False):
    if not settings.debugger:
        return
<<<<<<< Updated upstream
    if not settings.debugger.reactivate:
        backup = mouse.pos(), mouse.clicked()
    else:
        backup = settings.mouse_position, settings.mouse_clicked

    settings.mouse_position = None
    settings.mouse_clicked = None

=======
    if not reactivate:
        settings.debugger.start_mouse_position = mouse.pos()
        settings.debugger.start_enable_spoof = settings.enable_spoof
        settings.debugger.start_mouse_position_spoof = settings.mouse_position
    settings.enable_spoof = False
>>>>>>> Stashed changes
    settings.debugger.before_run()
    while settings.debugger.active:
        settings.debugger.update()
    if settings.debugger.reactivate:
        settings.mouse_position, settings.mouse_clicked = backup
    settings.debugger.after_run()
    if settings.debugger.reactivate:
        settings.enable_spoof = True
        settings.mouse_position = settings.debugger.start_mouse_position
    else:
        settings.enable_spoof = settings.debugger.start_enable_spoof
        settings.mouse_position = settings.debugger.start_mouse_position_spoof

    if delete_after:
        del settings.debugger
        settings.debugger = None
    else:
        settings.debugger.reset()


def start_recording():
    del settings.recording_data
    settings.recording_data = [display.display_reference.size]
    settings.recording = True


def stop_recording():
    settings.recording = False
    settings.recording_data[0] = display.display_reference.size
    if settings.debugger:
        if settings.debugger.reactivate:
            settings.debugger.reactivate = False
<<<<<<< Updated upstream
            start_debug()
=======
            start_debug(reactivate = True)
>>>>>>> Stashed changes
