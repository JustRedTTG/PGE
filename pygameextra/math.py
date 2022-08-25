import pygame

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
