import pygame
import math

def center(rect: tuple):
    return rect[0]+rect[2]*.5, rect[1]+rect[3]*.5


def lerp(point_a, point_b, length):
    a = pygame.math.Vector2(point_a)
    b = pygame.math.Vector2(point_b)
    something = b - a
    try:
        something.normalize_ip()
    except:
        pass
    something *= length
    destination = a + something
    return destination


def dist(point_a, point_b):
    return math.sqrt(((point_a[0] - point_b[0]) ** 2) + ((point_a[1] - point_b[1]) ** 2))


def perlin_noise():
    pass
