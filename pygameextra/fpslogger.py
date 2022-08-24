import time
import pygame
import pygameextra.time
import pygameextra.display


class logger:
    surface = None
    watch = {}
    last_label = ''

    def __init__(self, font, size, position):
        self.font = pygame.font.Font(font, size)
        self.good = 50
        self.okay = 30
        self.pos = position
        self.clock = pygameextra.time.clock
        self.renderTime = time.time() - 2

    def render(self):
        if time.time()-self.renderTime > 1:
            fps = self.clock.get_fps()
            text = str(int(fps) or 'Pygame Extra - logger')
            self.surface = self.font.render(text, True, (20, 200, 20) if fps >= self.good else (200, 200, 20) if fps >= self.okay else (200, 20, 20) if fps != 0 else (150, 206, 255), None if fps != 0 else (47, 123, 189))
            self.renderTime = time.time()
        pygameextra.display.blit(self.surface, self.pos)

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