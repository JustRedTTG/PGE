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


class AtlasSheetHandler(SheetHandler):
    def __init__(self, atlas: 'Atlas', sheet_key: int):
        self.atlas = atlas
        self.sheet_key = sheet_key

    def map(self, surface):
        pass


class Atlas:
    """The atlas is a all-in-one sheet manager, it combines a single texture file into multiple sheets
    """

    def __init__(self, file: AtlasFileType, mappings: dict = None):
        if isinstance(file, AtlasFile):
            self.atlas_file = file
        else:
            self.atlas_file = AtlasFile(file, mappings)

    @property
    def surface(self):
        return self.atlas_file.surface

    @property
    def mappings(self):
        return self.atlas_file.mappings

    @classmethod
    def from_atlas_file(cls, file: str):
        pass

    @classmethod
    def from_sheets(cls, sheets: dict):
        surfaces = []
        for key, sheet in sheets.items():
            for index in range(sheet.frames):
                mapping = sheet.handler.get(index)
                surfaces.append((key, Surface(mapping[2:]), index))
                with surfaces[-1][1]:
                    display.blit(sheet.surface, area=mapping)

        print(pack_surfaces(surfaces))

