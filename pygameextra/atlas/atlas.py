import pickle
from functools import lru_cache
from types import FunctionType
from typing import Union, List, Tuple, TypedDict, Dict

from pygameextra import display, Rect
from pygameextra.atlas.atlas_packing import pack_surfaces
from pygameextra.modified import SurfaceFileType, get_surface_file, CompressedSurface, Surface
from pygameextra.sheet import Sheet
from pygameextra.sheet_handlers import PropertySheetHandler, SheetMappingType


class AtlasSheetConfiguration(TypedDict):
    speed: float
    loop: bool
    pong: bool
    custom_offset_function: FunctionType
    custom_offset_function_data: dict


class AtlasFile:
    def __init__(self, file: SurfaceFileType, mappings: Dict[str, SheetMappingType],
                 sheet_configurations: Dict[str, AtlasSheetConfiguration] = None):
        self.surface = get_surface_file(file)
        self.mappings = mappings
        self.sheet_configurations = sheet_configurations or {}

    @classmethod
    def load(cls, file: str):
        with open(file, 'rb') as file:
            data = pickle.load(file)
        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(CompressedSurface.from_dict(data['file']).decompress(), data['mapping'],
                   data['sheet_configurations'])

    def save(self, save_location: str):
        with open(save_location, 'wb') as file:
            pickle.dump(self.to_dict(), file)

    def to_dict(self):
        compressed = self.surface.compress()

        return {'file': compressed.to_dict(), 'mapping': self.mappings,
                'sheet_configurations': self.sheet_configurations or {}
                }


AtlasFileType = Union[SurfaceFileType, AtlasFile]


class AtlasSheet(Sheet):
    def __init__(self, atlas: 'Atlas', key: str):
        self.atlas = atlas
        self.key = key

        self.__speed = self.atlas.sheet_configurations.get(key, {}).get('speed', 0)
        self._pong = self.atlas.sheet_configurations.get(key, {}).get('pong', False)
        self._loop = self.atlas.sheet_configurations.get(key, {}).get('loop', False)

        self.handler = PropertySheetHandler(lambda: self.atlas.mappings[self.key])

    @property
    def surface(self):
        return self.atlas.surface

    @property
    def _speed(self):
        return self.__speed

    @_speed.setter
    def _speed(self, value):
        self.__speed = value
        self.atlas.sheet_configurations[self.key]['speed'] = value

    @property
    def pong(self):
        return self._pong

    @pong.setter
    def pong(self, value):
        self._pong = value
        self.atlas.sheet_configurations[self.key]['pong'] = value

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value):
        self._loop = value
        self.atlas.sheet_configurations[self.key]['loop'] = value

    def configure(self, speed: float = None, loop: bool = None, pong: bool = None):
        self.speed = speed or self.speed
        self.loop = loop or self.loop
        self.pong = pong or self.pong

        return self

    def configure_from_dict(self, config: AtlasSheetConfiguration):
        self.configure(config['speed'], config['loop'], config['pong'])

        return self

    def handle_custom_offset(self, rect, sprite: 'Sprite'):
        custom_offset_function = self.atlas.sheet_configurations[self.key]['custom_offset_function']
        custom_offset_function_data = self.atlas.sheet_configurations[self.key]['custom_offset_function_data'] or {}
        return custom_offset_function(rect, sprite, custom_offset_function_data) if custom_offset_function is not None else rect


class Atlas:
    """The atlas is a all-in-one sheet manager, it combines a single texture file into multiple sheets
    """

    def __init__(self, file: AtlasFileType, mappings: dict = None,
                 sheet_configurations: Dict[str, AtlasSheetConfiguration] = None):
        if isinstance(file, AtlasFile):
            self._atlas_file = file
        elif not mappings:
            raise ValueError(
                "Mappings must be provided if file is not an AtlasFile. Use load for loading from a PGE atlas file.")
        else:
            self._atlas_file = AtlasFile(file, mappings, sheet_configurations)

    @property
    def surface(self):
        return self._atlas_file.surface

    @property
    def mappings(self):
        return self._atlas_file.mappings

    @property
    def sheet_configurations(self):
        return self._atlas_file.sheet_configurations

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

        # noinspection PyTypeChecker
        return cls(surface, mappings, {
            key: {'speed': sheet.speed * (2 if sheet.pong else 1), 'loop': sheet.loop, 'pong': sheet.pong,
                  'custom_offset_function': sheet.custom_offset if issubclass(type(sheet), Sheet) else None,
                  'custom_offset_function_data': sheet.data if issubclass(type(sheet), Sheet) else None
                  }
            for key, sheet in sheets.items()
        })

    def save(self, atlas_file: str):
        self._atlas_file.save(atlas_file)

    def export(self, image_file: str, mapping_file: str):
        raise NotImplementedError("Exporting to separate image and mapping files is not yet defined.")

    @classmethod
    def load(cls, file: str):
        return cls(AtlasFile.load(file))


    @classmethod
    @lru_cache
    def load_store(cls, file: str):
        return cls(AtlasFile.load(file))

    @classmethod
    def from_dict(cls, data: dict):
        return cls(AtlasFile.from_dict(data))

    def to_dict(self):
        return self._atlas_file.to_dict()

    @lru_cache
    def _access_atlas_sheet(self, key):
        return AtlasSheet(self, key)

    def __getitem__(self, key):
        if key in self.mappings:
            return self._access_atlas_sheet(key)
        super().__getitem__(key)
