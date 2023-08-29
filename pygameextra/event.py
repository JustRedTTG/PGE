"""PYGAME EXTRA Event script
This script manages all event actions"""

import pygame
import time
import pygameextra.settings as settings
import pygameextra.display as display

c: pygame.event.Event
event_buffer: list[pygame.event.Event, ...]


def Pquit() -> None:
    pygame.quit()
    exit()


def resizeCheck() -> bool:
    return c.type == pygame.WINDOWRESIZED


def buttonLocking() -> None:
    if settings.button_lock:
        if time.time() - settings.button_lock >= settings.button_lock_timeout_time:
            if settings.button_lock_hold:
                # TODO: potential optimization available
                if not pygame.mouse.get_pressed()[0]:
                    settings.button_lock = None
            else:
                settings.button_lock = None


def hoverLocking() -> None:
    if settings.hover_lock:
        if time.time() - settings.hover_lock >= settings.hover_lock_timeout_time:
            settings.hover_lock = None


def resizeCheckAuto() -> None:
    info = resizeCheck()
    if info:
        display.display_reference.size = display.display_reference.surface.get_size()
    return info


def rundown() -> None:
    global c, event_buffer
    if not settings.rundown_enabled: return
    buttonLocking()
    hoverLocking()
    for c in event_buffer:
        resizeCheckAuto()


def get() -> list[pygame.event.Event]:
    global event_buffer
    event_buffer = pygame.event.get()
    rundown()
    return event_buffer


def quitCheck() -> bool:
    global c
    """quitcheck() -> bool
    Checks if the window was attempted to be closed and returns a bool accordingly
    """
    return c.type == pygame.QUIT


def quitCheckAuto() -> None:
    global c
    """quitcheckauto() -> None
    Checks if the window has been closed and automatically quits the program
    """
    if quitCheck():
        Pquit()


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
