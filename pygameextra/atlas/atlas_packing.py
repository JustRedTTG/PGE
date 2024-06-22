from typing import List, Tuple

from pygameextra.modified import Surface
from pygameextra.rect import Rect
from pygameextra.touchingperimeter import Packer, Box
from pygameextra import settings


def expand_free_rects(previous_rects: List[Rect], previous_size: Tuple[int, int], new_size: Tuple[int, int]):
    new_rects = []
    difference_in_size = tuple(new - previous for new, previous in zip(new_size, previous_size))

    for previous_rect in previous_rects:
        new_rect: Rect = previous_rect.copy()
        if previous_rect.right == previous_size[0]:
            new_rect.w += difference_in_size[0]
        if previous_rect.bottom == previous_size[1]:
            new_rect.h += difference_in_size[1]
        new_rects.append(new_rect)

    right_column_available = False
    bottom_row_available = False
    edge_available = False

    for rect in new_rects:
        if rect.left == previous_size[0] and rect.top == 0 and rect.right == new_size[0] and rect.height == new_size[1]:
            right_column_available = True
        elif rect.left == 0 and rect.top == previous_size[1] and rect.width == new_size[0] and rect.bottom == new_size[
            1]:
            bottom_row_available = True
        elif rect.left == previous_size[0] and rect.top == previous_size[1] and rect.right == new_size[
            0] and rect.bottom == new_size[1]:
            edge_available = True

    if not right_column_available:
        new_rects.append(Rect(previous_size[0], 0, new_size[0] - previous_size[0], new_size[1]))
    if not bottom_row_available:
        new_rects.append(Rect(0, previous_size[1], new_size[0], new_size[1] - previous_size[1]))
    if not edge_available:
        new_rects.append(Rect(previous_size[0], previous_size[1], new_size[0] - previous_size[0],
                              new_size[1] - previous_size[1]))

    return new_rects


def try_pack(rects: List[Rect], size: Tuple[int, int], previous_result: List[Rect] = None):
    bin = Rect(0, 0, *size)
    packer = Packer(bin)
    queue = rects.copy()

    if previous_result is not None:
        packer.packed, packer.free_rects = previous_result[0], expand_free_rects(*previous_result[1:], size)
        queue = queue[len(packer.packed):]

    while queue:
        rect = queue.pop(0)
        if not packer.pack(Box(rect.width, rect.height)):
            return False, [packer.packed, packer.free_rects, size], rect

    for packed_rect, rect in zip(packer.packed, rects):
        rect.x = packed_rect.x
        rect.y = packed_rect.y

    return True, rects


def pack(rects: List[Rect], size: Tuple[int, int]):
    previous_result = None
    extending_side = True
    while not (result := try_pack(rects, size, previous_result))[0]:
        if result[2].width == result[2].height:
            add_width = extending_side
        else:
            add_width = result[2].width < result[2].height
        if add_width and size[0] > size[1]:
            add_width = not add_width
        add_height = not add_width
        extending_side = not extending_side

        size = (
            size[0] + result[2].width * (1 if add_width else 0),
            size[1] + result[2].height * (1 if add_height else 0))
        if settings.atlas_attempt_keep_past_attempt:
            previous_result = result[1]
    return result[1], size


def pack_surfaces(surfaces: List[Tuple[str, Surface, int]], existing_mappings: dict = None):
    # Sort the surfaces by the largest dimension, to pack the largest surfaces first
    surfaces.sort(key=lambda surface: surface[1].width * surface[1].height, reverse=True)

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
    packing_map, size = pack(rects, begin_size)

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

    return mappings, size
