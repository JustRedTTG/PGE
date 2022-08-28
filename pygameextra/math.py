import math
# noinspection PyUnresolvedReferences
from perlin_noise import PerlinNoise


def center(rect: tuple):
    return rect[0]+rect[2]*.5, rect[1]+rect[3]*.5


def dist(point_a: tuple, point_b: tuple):
    return math.sqrt(((point_a[0] - point_b[0]) ** 2) + ((point_a[1] - point_b[1]) ** 2))


def lerp(point_a: tuple, point_b: tuple, length: [int, float]):
    return point_a[0] + length * (point_b[0] - point_a[0]), point_a[1] + length * (point_b[1] - point_a[1])
