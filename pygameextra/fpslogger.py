import time
import os
import pygame
import pygameextra.time
import pygameextra.display
import pygameextra.colors as colors

location = os.path.dirname(os.path.realpath(__file__))


class Logger:
    surface = None
    watch = {}
    last_label = ''
    total = 1
    count = 1

    def __init__(self, font: str = os.path.join(location, 'font.ttf'), size: int = 15, position: tuple = None):
        self.font = pygame.font.Font(font, size)
        self.good = 50
        self.okay = 30
        self.pos = position
        self.clock = pygameextra.time.clock
        self.renderTime = time.time() - 2

    def render(self):
        if time.time()-self.renderTime > 1:
            fps = self.clock.get_fps()
            text = str(int(fps) or 'Pygame Extra - logger') + (f' / {int(self.total/self.count)}' if fps > 0 else '')
            if fps != 0:
                self.total += fps
                self.count += 1
            self.surface = self.font.render(text, True, (20, 200, 20) if fps >= self.good else (200, 200, 20) if fps >= self.okay else (200, 20, 20) if fps != 0 else colors.pge_light, None if fps != 0 else colors.pge_dark)
            self.renderTime = time.time()
        pygameextra.display.blit(self.surface, self.pos or (
            10, pygameextra.display.get_height()-10-self.font.get_height()
        ))

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