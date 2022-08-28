"""PYGAME EXTRA Event script
This script manages all event actions"""

import pygame
import time
import pygameextra.settings as settings
import pygameextra.display as display

c = pygame.event.Event
event_buffer = []


def Pquit():
    pygame.quit()
    exit()


def resizeCheck():
    global c
    return c.type == pygame.WINDOWRESIZED


def buttonLocking():
    if settings.button_lock:
        if time.time()-settings.button_lock >= settings.button_timeout_time:
            if settings.button_lock_hold:
                if not pygame.mouse.get_pressed()[0]:
                    settings.button_lock = None
            else:
                settings.button_lock = None


def resizeCheckAuto():
    info = resizeCheck()
    if info:
        display.display_reference.size = display.display_reference.surface.get_size()
    return info


def rundown():
    global c, event_buffer
    if not settings.enable_rundown: return
    buttonLocking()
    for c in event_buffer:
        resizeCheckAuto()


def get():
    global event_buffer
    event_buffer = pygame.event.get()
    rundown()
    return event_buffer


def quitcheck():
    global c
    """quitcheck() -> Bool
    Checks if the window was attempted to be closed and returns a bool accordingly
    """
    return c.type == pygame.QUIT


def quitcheckauto():
    global c
    """quitcheckauto() -> None
    Checks if the window has been closed and automatically quits the program
    """
    if quitcheck():
        Pquit()


def keylog():
    global c
    """keylog() -> int
    Returns all the button pressed or released
    """
    if c.type == pygame.KEYDOWN or c.type == pygame.KEYUP:
        return c.key


def key_UP(var):
    global c
    """key_UP(key) -> Bool
    Check if a button has been released and returns a bool accordingly
    """
    if c.type == pygame.KEYUP:
        return c.key == var


def key_DOWN(var):
    global c
    """key_DOWN(key) -> Bool
    Checks if a key is pressed and returns a bool accordingly
    """
    if c.type == pygame.KEYDOWN:
        return c.key == var
