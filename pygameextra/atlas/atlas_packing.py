from typing import List, Tuple

from pygameextra import Surface
from pygameextra.touchingperimeter import Packer

def pack_surfaces(surfaces: List[Tuple[str, Surface, int]], existing_mappings: dict = None):
    surfaces.sort(key=lambda surface: max(surface[1].width, surface[1].height), reverse=True)

    keys = set(surface[0] for surface in surfaces)
    mappings = {**(existing_mappings or {}), **{key: [] for key in keys}}

    begin_size = list(surfaces[0][1].size)
