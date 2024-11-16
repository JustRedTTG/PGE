"""Pygame Extra's rect function"""
from numbers import Number
import pygame


class Rect(pygame.Rect):
    """rect(a, b, c, d) -> Rect Object
    A simple rect function :P
    """

    # noinspection PyTypeChecker
    def __init__(self, x: Number, y: Number, width: Number, height: Number):
        super().__init__(x, y, width, height)
