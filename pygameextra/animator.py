"""PYGAME EXTRA Sheet script
This script manages the animator class"""
from typing import Union

from pygameextra.sheet import Sheet
from functools import lru_cache
from frozendict import frozendict


class Animator:
    _config: dict
    one_to_one_rules: dict = {}
    key_values: dict = {}
    many_to_one_rules: dict = {}

    def __init__(self, config: dict):
        self.key_values = {}
        self.width = 0
        self.height = 0
        self.config = config

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config):
        self.one_to_one_rules = {}
        self.many_to_one_rules = {}
        self._get_sheet.cache_clear()

        for key, value in config.items():
            if type(key) is str and (type(value) is str or type(value) is Sheet):
                self.one_to_one_rules[key] = value
                self.key_values[key] = self.key_values.get(key, False)
            elif type(key) == tuple and (type(value) == str or type(value) == Sheet):
                self.many_to_one_rules[key] = value
                for sub_key in key:
                    self.key_values[sub_key] = self.key_values.get(sub_key, False)
            if type(value) is Sheet:
                self.width = value.handler.width
                self.height = value.handler.height

        self._config = {**self.one_to_one_rules, **self.many_to_one_rules}

    def __setattr__(self, key, value):
        if key not in self.key_values.keys():
            return super().__setattr__(key, value)
        if type(value) != bool:
            raise TypeError("Values passed to the animator's switches should be of type bool")
        self.key_values[key] = value

    def __getattr__(self, key):
        try:
            return super().__getattribute__(key)
        except AttributeError:
            pass

        class Item:
            # noinspection PyMethodParameters
            def __setattr__(temporary_item, extra_key, value):
                self.__setattr__(f'{key}{extra_key}', value)

            # noinspection PyMethodParameters
            def __getattr__(temporary_item, extra_key):
                return self.__getattr__(f'{key}{extra_key}')

            def __setitem__(temporary_item, extra_key, value):
                self.__setattr__(f'{key}{extra_key}', value)

        return Item()

    @lru_cache()
    def _get_sheet(self, key_values: frozendict):
        sheet_dict = 'many_to_one_rules'
        for keys, value in self.many_to_one_rules.items():
            for key in keys:
                if not key_values.get(key, False):
                    break
            else:
                return sheet_dict, keys
        sheet_dict = 'one_to_one_rules'
        for key, value in self.one_to_one_rules.items():
            if key_values.get(key, False):
                return sheet_dict, key

        return None, None

    @lru_cache()
    def _final_sheet(self, sheet_value):
        if type(sheet_value) is Sheet:
            return sheet_value
        elif type(sheet_value) is str:
            return self._final_sheet(self.one_to_one_rules[sheet_value])

    def get_sheet(self) -> Union[Sheet, None]:
        sheet_dict, sheet_key = self._get_sheet(frozendict(self.key_values))
        if not sheet_dict:
            return None
        return self._final_sheet(super().__getattribute__(sheet_dict)[sheet_key])

    @property
    def surface(self):
        sheet = self.get_sheet()
        if sheet:
            return sheet.surface

    @property
    def frames(self):
        sheet = self.get_sheet()
        if sheet:
            return sheet.frames

    def get(self, sprite: 'Sprite'):
        sheet: Sheet = self.get_sheet()
        if sprite.index > sheet.frames:
            sprite.index = sprite.index % sheet.frames
        if sheet:
            return sheet.get(sprite)

    @property
    def speed(self):
        try:
            return self.get_sheet().speed
        except AttributeError:
            return None
