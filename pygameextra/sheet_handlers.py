"""PYGAME EXTRA Sprite sheet handlers script
This script manages all sprite sheet functions"""
from pygameextra.modified import Surface


class sheet_handler:
    width = 0
    height = 0
    mapping = {}
    offset = (0, 0)
    def __init__(self): pass

    def map(self, surface): pass

    def get(self, sprite): pass

    def add(self, x, y): return x, y

# noinspection PyMissingConstructor
class SHEET_VERTICAL(sheet_handler):
    def __init__(self, width_of_cell: int = 1, height_of_cell: int = 1, offset_x: int = 0, offset_y: int = 0):
        self.width = width_of_cell
        self.height = height_of_cell
        self.offset = (offset_x, offset_y)

    def map(self, surface: Surface):
        x, y = self.offset
        self.mapping = {}
        i = 0
        while x < surface.size[0]:  # Goes through each X position
            while y < surface.size[1]:  # Gets a map of all Y objects it can
                self.mapping[i] = self.add(x, y)  # Map it
                y += self.height  # Increment
            x += self.width  # Increment
            y = self.offset[1]  # Reset

    def get(self, sprite): return self.mapping[int(sprite.index)]


# noinspection PyMissingConstructor
class SHEET_HORIZONTAL(sheet_handler):
    def __init__(self, width_of_cell: int = 1, height_of_cell: int = 1, offset_x: int = 0, offset_y: int = 0):
        self.width = width_of_cell
        self.height = height_of_cell
        self.offset = (offset_x, offset_y)

    def map(self, surface: Surface):
        x, y = self.offset
        self.mapping = {}
        i = 0
        while y < surface.size[0]:  # Goes through each X position
            while x < surface.size[1]:  # Gets a map of all Y objects it can
                self.mapping[i] = self.add(x, y)  # Map it
                x += self.width  # Increment
            x = self.offset[0]  # Reset
            y += self.height  # Increment

    def get(self, sprite): return self.mapping[int(sprite.index)]
