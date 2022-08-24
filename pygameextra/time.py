import pygame
import pygameextra.settings as settings

clock = None
framerate = None
tickBlock = False

def init():
    global clock
    clock = pygame.time.Clock()


def tick(fps: int = None):
    if tickBlock:
        settings.auto_fps = False
    clock.tick(fps or framerate or 0)