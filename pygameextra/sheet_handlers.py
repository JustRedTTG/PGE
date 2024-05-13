"""PYGAME EXTRA Sprite sheet handlers script
This script manages all sprite sheet functions"""
from abc import abstractmethod, ABC
from typing import List, Tuple

from pygameextra.modified import Surface

SheetMappingType = List[Tuple[int, int, int, int]]


class SheetHandler(ABC):
    mapping: SheetMappingType = []
    width: int
    height: int

    @abstractmethod
    def map(self, surface): pass

    def get(self, index): return self.mapping[int(index)]


class GenericSheetHandler(SheetHandler, ABC):

    def __init__(self,
                 width_of_cell: int = 1, height_of_cell: int = 1,
                 offset_x: int = 0, offset_y: int = 0,
                 spacing_x: int = 0, spacing_y: int = 0):
        self.width = width_of_cell
        self.height = height_of_cell
        self.offset = (offset_x, offset_y)
        self.spacing = (spacing_x, spacing_y)

    def _add(self, x, y): return x, y, self.width, self.height


class SheetVertical(GenericSheetHandler):
    def map(self, surface: Surface):
        x, y = self.offset
        self.mapping = []
        i = 0
        while x < surface.size[0]:  # Goes through each X position
            while y < surface.size[1]:  # Gets a map of all Y objects it can
                self.mapping.append(self._add(x, y))  # Map it
                y += self.height + self.spacing[1]  # Increment
                i += 1
            x += self.width + self.spacing[0]  # Increment
            y = self.offset[1]  # Reset


class SheetHorizontal(GenericSheetHandler):

    def map(self, surface: Surface):
        x, y = self.offset
        self.mapping = []
        i = 0
        while y < surface.size[1]:  # Goes through each Y position
            while x < surface.size[0]:  # Gets a map of all X objects it can
                self.mapping.append(self._add(x, y))  # Map it
                x += self.width + self.spacing[0]  # Increment
                i += 1
            x = self.offset[0]  # Reset
            y += self.height + self.spacing[1]  # Increment


class PropertySheetHandler(SheetHandler):

    def __init__(self, mapping_getter=None):
        self.mapping_getter = mapping_getter
        self.width = self.mapping[0][2]
        self.height = self.mapping[0][3]

    def map(self, surface: Surface):
        pass

    @property
    def mapping(self):
        return self.mapping_getter()
