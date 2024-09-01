"""PYGAME EXTRA Event script
This script manages all event actions"""
import sys
from typing import List

import pygame
import time
import pygameextra.settings as settings
import pygameextra.display as display
from pygameextra._deprecations import EVENT_NAMES_DEPRECATION_WRAPPER

Event = pygame.event.Event
c: Event
event_buffer: List[Event]


def pge_quit() -> None:
    pygame.quit()
    sys.exit()


Pquit = EVENT_NAMES_DEPRECATION_WRAPPER(pge_quit)


def resize_check() -> bool:
    return c.type == pygame.WINDOWRESIZED


resizeCheck = EVENT_NAMES_DEPRECATION_WRAPPER(resize_check)


def button_locking() -> None:
    if settings.button_lock:
        if time.time() - settings.button_lock >= settings.button_lock_timeout_time:
            if settings.button_lock_hold:
                # TODO: potential optimization available
                if not pygame.mouse.get_pressed()[0]:
                    settings.button_lock = None
            else:
                settings.button_lock = None


buttonLocking = EVENT_NAMES_DEPRECATION_WRAPPER(button_locking)


def hover_locking() -> None:
    if settings.hover_lock:
        if time.time() - settings.hover_lock >= settings.hover_lock_timeout_time:
            settings.hover_lock = None


hoverLocking = EVENT_NAMES_DEPRECATION_WRAPPER(hover_locking)


def resize_check_auto() -> None:
    info = resize_check()
    if info:
        display.display_reference.size = display.display_reference.surface.get_size()
    return info


resizeCheckAuto = EVENT_NAMES_DEPRECATION_WRAPPER(resize_check_auto)


def rundown() -> None:
    global c, event_buffer
    if not settings.rundown_enabled: return
    button_locking()
    hover_locking()
    for c in event_buffer:
        resize_check_auto()


def get() -> list[pygame.event.Event]:
    global event_buffer
    event_buffer = pygame.event.get()
    rundown()
    return event_buffer


def quit_check() -> bool:
    global c
    """quitcheck() -> bool
    Checks if the window was attempted to be closed and returns a bool accordingly
    """
    return c.type == pygame.QUIT


quitCheck = EVENT_NAMES_DEPRECATION_WRAPPER(quit_check)


def quit_check_auto() -> None:
    global c
    """quitcheckauto() -> None
    Checks if the window has been closed and automatically quits the program
    """
    if quit_check():
        pge_quit()


quitCheckAuto = EVENT_NAMES_DEPRECATION_WRAPPER(quit_check_auto)


def keylog() -> int:
    global c
    """keylog() -> int
    Returns all the button pressed or released
    """
    if c.type == pygame.KEYDOWN or c.type == pygame.KEYUP:
        return c.key


def key_UP(var) -> bool:
    global c
    """key_UP(key) -> bool
    Check if a button has been released and returns a bool accordingly
    """
    if c.type == pygame.KEYUP:
        return c.key == var


def key_DOWN(var) -> bool:
    global c
    """key_DOWN(key) -> bool
    Checks if a key is pressed and returns a bool accordingly
    """
    if c.type == pygame.KEYDOWN:
        return c.key == var
