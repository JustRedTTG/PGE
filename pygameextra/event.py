"""PYGAME EXTRA Event script
This script manages all event actions"""

import pygame

c = None
event_buffer = None

def Pquit():
    pygame.quit()
    exit()

def get():
    event_buffer = pygame.event.get()
    return event_buffer

def quitcheck():
    """quitcheck() -> Bool
    Checks if the window was attempted to be closed and returns a bool accordingly
    """
    return c.type == pygame.QUIT

def quitcheckauto():
    """quitcheckauto() -> None
    Checks if the window has been closed and automatically quits the program
    """
    if quitcheck(): Pquit()
        
def keylog():
    """keylog() -> int
    Returns all the button pressed or released
    """
    if c.type == pygame.KEYDOWN or c.type == pygame.KEYUP: return c.key
def key_UP(var):
    """key_UP(key) -> Bool
    Check if a button has been released and returns a bool accordingly
    """
    if c.type == pygame.KEYUP: return c.key == var
def key_DOWN(var):
    """key_DOWN(key) -> Bool
    Checks if a key is pressed and returns a bool accordingly
    """
    if c.type == pygame.KEYDOWN: return c.key == var