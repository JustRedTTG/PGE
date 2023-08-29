import time
import os
import pygame
import pygameextra.time
import pygameextra.display
import pygameextra.colors as colors
import pygameextra.recorder as recorder
from pygameextra.modified import Surface
from pygameextra.fill import transparency as fill_trans

location = os.path.dirname(os.path.realpath(__file__))


class Logger:
    surface = None
    watch = {}
    last_label = ''
    total = 0
    count = 0

    def __init__(self, font: str = os.path.join(location, 'font.ttf'), size: int = 15, position: tuple = None):
        self.font = pygame.font.Font(font, size)
        self.good = 50
        self.okay = 30
        self.pos = position
        self.clock = pygameextra.time.clock
        self.renderTime = time.time() - 2

    def render(self):
        recorder.comment(f"FPS logger : {self}")
        if time.time() - self.renderTime > 1:
            fps = self.clock.get_fps()
            text = str(int(fps) or 'Pygame Extra ') + (
                f' / {int(self.total / self.count)}' if self.count > 0 else ' Loading...')
            if fps != 0:
                self.total += fps
                self.count += 1
                if self.count > 20:
                    self.total = fps
                    self.count = 1
            self.surface = self.font.render(text, True, (20, 200, 20) if fps >= self.good else (
            200, 200, 20) if fps >= self.okay else (200, 20, 20) if fps != 0 else colors.pge_light,
                                            None if fps != 0 else colors.pge_dark)
            back_surface = Surface(self.surface.get_size())
            fill_trans(colors.black, 150, back_surface)
            back_surface.stamp(self.surface)
            self.surface = back_surface
            self.renderTime = time.time()
        pygameextra.display.blit(self.surface, self.pos or (
            10, pygameextra.display.get_height() - 10 - self.font.get_height()
        ))
        recorder.padding_comment()

    def resetwatch(self, label: str = 'stopwatch'):
        self.watch[label] = time.time()

    def stopwatch(self, label: str = 'stopwatch'):
        if self.last_label == label:
            print('\r', end='')
        else:
            print()
        self.last_label = label
        print(f'Pygame Extra, {label}: {time.time() - self.watch[label]:.03f}', end='')
        self.resetwatch(label)
