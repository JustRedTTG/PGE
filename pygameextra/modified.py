"""PYGAME EXTRA Modifications script
This script manages all pygame modifications"""
import zlib
import pygame

from pygameextra import display, mouse
from pygameextra.rect import Rect
from pygameextra.sorters import layer_sorter
from typing import Union, IO, List, Literal

_string_format = Literal["P", "RGB", "RGBX", "RGBA", "ARGB", "BGRA"]


class SurfaceException(Exception):
    pass


class CompressedSurface:
    def __init__(
            self,
            file: 'SurfaceFileType',
            level: int = zlib.Z_BEST_COMPRESSION,
            image_format: _string_format = 'RGBA'):
        surface = get_surface_file(file)
        self.format: _string_format = image_format
        self.compressed = zlib.compress(pygame.image.tobytes(surface.surface, self.format), level=level)
        self.size = surface.size

    def decompress(self) -> 'Surface':
        return Surface(surface=pygame.image.frombytes(zlib.decompress(self.compressed), self.size, self.format))

    def to_dict(self) -> dict:
        return {
            'compressed': self.compressed,
            'format': self.format,
            'size': self.size
        }

    @classmethod
    def from_dict(cls, raw: dict) -> 'CompressedSurface':
        instance = cls.__new__(cls)
        instance.compressed = raw['compressed']
        instance.format = raw['format']
        instance.size = raw['size']
        return instance


class Surface:
    surface: pygame.Surface
    size: tuple
    layer: int
    display_tag: False

    def __init__(self, size: tuple = (0, 0), layer: int = 0, surface: pygame.Surface = None):
        if surface:
            self.size = surface.get_size()
            self.surface = surface
            self.layer = layer
        else:
            self.size = size
            self.surface = pygame.Surface(size, pygame.SRCALPHA)
            self.layer = layer
        self.area = None  # Used by stamps function
        self.pos = None  # Used by stamps function
        self.frames = 1  # Used by sprite animation function, if used improperly
        self._offset: mouse.Offset = None
        self._display_backup: Surface = None
        self._with_depth = 0
        self.last_blit_pos = (0, 0)


    def stamp(self, source: Union['Surface', pygame.Surface], position: tuple = (0, 0), area: tuple = None,
              special_flags: int = 0):
        if type(source) is pygame.Surface:
            self.surface.blit(source, position, area, special_flags)
        else:
            self.surface.blit(source.surface, position, area, special_flags)

    def stamps(self, sources: List[Union['Surface', pygame.Surface]], positions: List[tuple] = None,
               areas: List[tuple] = None, special_flags: int = 0):
        if not positions:
            positions = [(0, 0)] * len(sources)
        if not areas:
            areas = [None] * len(sources)
        for i in range(len(sources)):
            sources[i].pos = positions[i]
            sources[i].area = areas[i]
        sources.sort(key=layer_sorter)
        for source in sources:
            self.surface.blit(source.surface, source.area, special_flags)

    def bind(self, layer: int):
        if self.layer >= 0 and layer >= 0:
            self.layer = layer
        elif layer < 0:
            raise SurfaceException("Can't bind a surface to a display surface layer.")
        else:
            raise SurfaceException("Can't bind a display surface to a surface layer.")

    def resize(self, size: tuple):
        self.surface = pygame.transform.scale(self.surface, size)
        self.size = self.surface.get_size()

    def flip(self, flip_x: bool = False, flip_y: bool = False):
        self.surface = pygame.transform.flip(self.surface, flip_x, flip_y)

    def copy(self) -> 'Surface':
        return Surface(self.size, self.layer, self.surface.copy())

    def get_at(self, x_y: tuple) -> tuple:
        return self.surface.get_at(x_y)

    def set_at(self, x_y: tuple, color: tuple) -> None:
        return self.surface.set_at(x_y, color)

    def set_alpha(self, alpha: int, flags: int = 0) -> None:
        return self.surface.set_alpha(alpha, flags)

    @property
    def rect(self) -> pygame.Rect:
        return self.surface.get_rect()

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    def compress(self) -> CompressedSurface:
        return CompressedSurface(self.surface)

    def save_to_file(self, file: str):
        pygame.image.save(self.surface, file)

    def __enter__(self):
        if self._display_backup is not None:
            self._with_depth += 1
            return
        self._display_backup = display.display_reference
        self._offset = mouse.Offset(self.last_blit_pos, additive=True, reverse=True)
        display.context(self)
        self._offset.__enter__()
        self._with_depth = 0

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._with_depth > 0:
            self._with_depth -= 1
            return
        display.context(self._display_backup)
        self._display_backup = None
        self._offset.__exit__(exc_type, exc_val, exc_tb)


SurfaceFileType = Union[str, IO, Surface, pygame.Surface, CompressedSurface]


def transparent_surface(area: tuple, alpha: int):
    new_surface = Surface(area)
    new_surface.set_alpha(alpha)
    return new_surface


def get_surface_file(file: SurfaceFileType, layer: int = 0) -> Surface:
    try:
        return Surface(surface=pygame.image.load(file).convert_alpha(), layer=layer)
    except TypeError:
        pass
        if isinstance(file, Surface):
            return file
        elif isinstance(file, pygame.Surface):
            return Surface(surface=file, layer=layer)
        elif isinstance(file, CompressedSurface):
            return file.decompress()
        else:
            raise TypeError("Please make sure file is a path / surface / file-like object")
