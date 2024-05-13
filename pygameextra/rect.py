"""Pygame Extra's rect function"""
import pygame


class Rect:
    """rect(a, b, c, d) -> Rect Object
    A simple rect function :P
    """
    def __new__(cls, rect1, rect2, rect3, rect4):
        return pygame.Rect(rect1, rect2, rect3, rect4)
