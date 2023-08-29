"""A PI circle radius gwnwerator."""

from numpy import sin, cos, radians


class TSX:
    position: tuple
    radius: int
    offset: int

    def __init__(self, position: tuple, radius: int, offset: int = 0):
        self.position = position
        self.radius = radius
        self.offset = offset

    def __getitem__(self, rotation: int):
        rotation = radians(rotation + self.offset)
        x = self.position[0] + self.radius * cos(rotation)
        y = self.position[1] + self.radius * sin(rotation)
        return x, y
