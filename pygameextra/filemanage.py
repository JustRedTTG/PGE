import os, shutil


def folder(location: str, delete: bool = False):
    if not os.path.exists(location):
        os.mkdir(location)
    elif delete:
        shutil.rmtree(location)
        os.mkdir(location)


def check(location: str):
    return os.path.exists(location)
