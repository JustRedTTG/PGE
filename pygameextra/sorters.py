"""PYGAME EXTRA Sorters script
This script manages all PYGAME EXTRA exclusive sorting key functions"""


def layer_sorter(item):
    """Pygame Extra Layer sorter
    This is used with sort() builtin function. Returns the item's layer"""
    return item.layer
