"""PYGAME EXTRA Event script
This script manages all event actions"""
import sys
from typing import List, Union

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
                if not any(pygame.mouse.get_pressed()):
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


class Key:
    def __init__(self, event):
        self.unicode = event.unicode
        self.key = event.key

    def __hash__(self):
        return self.key

    def __eq__(self, other):
        if isinstance(other, Key):
            return self.key == other.key
        elif isinstance(other, int):
            return self.key == other
        return False

class KeyHold:
    KEY_PRESS_INITIAL_DELAY = .5
    HOLD_DELAY = .03

    def __init__(self):
        self.keys_down = {}

    def handle_event(self) -> Union[None, int]:
        global c 
        if c.type == pygame.KEYDOWN:
            capture = Key(c)
            self.keys_down[capture] = time.time() + self.KEY_PRESS_INITIAL_DELAY
            return capture
        elif c.type == pygame.KEYUP:
            try:
                del self.keys_down[c.key]
            except KeyError:
                pass

    def handle_hold(self) -> List[Key]:
        keys: List[Key] = []
        for key, pressed in self.keys_down.items():
            now = time.time()
            if now < pressed:
                continue
            while now >= pressed + self.HOLD_DELAY:
                pressed += self.HOLD_DELAY
                keys.append(key)
            self.keys_down[key] = pressed
        return keys
        
    