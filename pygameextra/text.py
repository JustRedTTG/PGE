import pygame
import os
from pygameextra import display
from functools import lru_cache

location = os.path.dirname(os.path.realpath(__file__))


@lru_cache()
def get_font(font, font_size):
    return pygame.font.Font(font, font_size)


class Text:
    obj = None
    rect = None

    def __init__(self, text: str = '-_-', font: [str, pygame.font.Font] = os.path.join(location, 'font.ttf'),
                 font_size: int = 3, position: tuple = (0, 0), colors: [tuple, list] = ((255, 255, 255), None),
                 antialias: bool = True):
        if isinstance(font, pygame.font.Font):
            self.font = font
        else:
            self.font = get_font(font, font_size)
        self.text = text
        self.position = position
        self.antialias = antialias
        self.color = colors[0]
        self.background = colors[1]
        self.init()

    def init(self):
        self.obj = self.font.render(self.text, self.antialias, self.color, self.background)
        self.rect = self.obj.get_rect()
        self.rect.center = self.position

    def display(self):
        display.blit(self.obj, self.rect)


def quick(text: str = '-_-', font_size: int = 3, position: tuple = (0, 0)):
    return Text(text, font_size=font_size, position=position, colors=((0, 0, 0), None))
