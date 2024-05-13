from typing import List, Tuple

from pygameextra.modified import Surface
from pygameextra.rect import Rect
from pygameextra.touchingperimeter import Packer, Box


def try_pack(rects: List[Rect], size: Tuple[int, int]):
    bin = Rect(0, 0, *size)
    packer = Packer(bin)
    queue = rects.copy()

    while queue:
        rect = queue.pop(0)
        if not packer.pack(Box(rect.width, rect.height)):
            return False, rect
        
    for packed_rect, rect in zip(packer.packed, rects):
        rect.x = packed_rect.x
        rect.y = packed_rect.y

    return True, rects


def pack(rects: List[Rect], size: Tuple[int, int]):
    while not (result := try_pack(rects, size))[0]:
        size = (size[0] + result[1].width // 2, size[1] + result[1].height // 2)
    return result[1]


def pack_surfaces(surfaces: List[Tuple[str, Surface, int]], existing_mappings: dict = None):
    # Sort the surfaces by the largest dimension, to pack the largest surfaces first
    surfaces.sort(key=lambda surface: max(surface[1].width, surface[1].height), reverse=True)

    # Initialize some basic information
    keys = set(surface[0] for surface in surfaces)
    mappings = existing_mappings or {}

    # Set a random starting size for the atlas
    begin_size = surfaces[0][1].size

    # Create a box object for each surface
    rects = [
        Rect(0, 0, *surface[1].size) for surface in surfaces
    ]

    # Store a reference to the surface for each rect
    surface_backref = {
        id(rect): surface for rect, surface in zip(rects, surfaces)
    }

    # Pack the rects
    packing_map = pack(rects, begin_size)

    # Create temporary mappings to clean up the packing map
    temporary_mappings = {key: [] for key in keys}

    for rect in packing_map:
        surface = surface_backref[id(rect)]
        # Temporarily map the rects to their surfaces to determine the key and get the index
        temporary_mappings[surface[0]].append((rect, surface[2]))

    # Sort the temporary mappings by the frame index
    for key in keys:
        mappings[key] = [
            *mappings.get(key, []),
            *[
                tuple(rect[0]) for rect in sorted(temporary_mappings[key], key=lambda x: x[1])
            ]
        ]

    return mappings
