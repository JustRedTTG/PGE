import pickle
from typing import Union, List, Tuple

from pygameextra import display, Rect
from pygameextra.atlas.atlas_packing import pack_surfaces
from pygameextra.modified import SurfaceFileType, get_surface_file, CompressedSurface, Surface
from pygameextra.sheet import Sheet
from pygameextra.sheet_handlers import SheetHandler


class AtlasFile:
    def __init__(self, file: SurfaceFileType, mappings: dict):
        self.surface = get_surface_file(file)
        self.mappings = mappings

    @classmethod
    def load(cls, file: str):
        with open(file, 'rb') as file:
            raw = pickle.load(file)
        return cls(CompressedSurface.from_dict(raw['file']).decompress(), raw['mapping'])

    @classmethod
    def save(cls, file: SurfaceFileType, mapping: dict, save_location: str):
        if isinstance(file, CompressedSurface):
            compressed = file
        else:
            compressed = get_surface_file(file).compress()

        with open(save_location, 'wb') as file:
            pickle.dump({'file': compressed.to_dict(), 'mapping': mapping}, file)


AtlasFileType = Union[SurfaceFileType, AtlasFile]


class AtlasSheet:
    pass


class Atlas:
    """The atlas is a all-in-one sheet manager, it combines a single texture file into multiple sheets
    """

    def __init__(self, file: AtlasFileType, mappings: dict = None):
        if isinstance(file, AtlasFile):
            self._atlas_file = file
        else:
            self._atlas_file = AtlasFile(file, mappings)

    @property
    def surface(self):
        return self._atlas_file.surface

    @property
    def mappings(self):
        return self._atlas_file.mappings

    @classmethod
    def from_sheets(cls, sheets: dict):
        surfaces = []
        for key, sheet in sheets.items():
            for index in range(sheet.frames):
                mapping = sheet.handler.get(index)
                surfaces.append((key, Surface(mapping[2:]), index))
                with surfaces[-1][1]:
                    display.blit(sheet.surface, area=mapping)

        mappings, size = pack_surfaces(surfaces)

        surface = Surface(size)

        with surface:
            for key, sheet in sheets.items():
                for index in range(sheet.frames):
                    mapping = sheet.handler.get(index)
                    display.blit(sheet.surface, mappings[key][index][:2], mapping)

        return cls(surface, mappings)

    def save(self, atlas_file: str):
        AtlasFile.save(self.surface, self.mappings, atlas_file)

    def export(self, image_file: str, mapping_file: str):
        pass

    @classmethod
    def load(cls, file: str):
        return cls(AtlasFile.load(file))
