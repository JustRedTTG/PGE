import math


# noinspection PyUnresolvedReferences
# from perlin_noise import PerlinNoise


def center(rect: tuple):
    return rect[0] + rect[2] * .5, rect[1] + rect[3] * .5


def dist(point_a: tuple, point_b: tuple):
    return math.sqrt(((point_a[0] - point_b[0]) ** 2) + ((point_a[1] - point_b[1]) ** 2))


def lerp(point_a: tuple, point_b: tuple, length: [int, float]):
    return (1 - length) * point_a[0] + length * point_b[0], (1 - length) * point_a[1] + length * point_b[1]


def lerp_legacy(point_a: tuple, point_b: tuple, length: [int, float]):
    return lerp(point_a, point_b, length / dist(point_a, point_b))
