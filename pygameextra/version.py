VERSION = '2.0.0'
revision = 9
beta = True


def get():
    return f'{VERSION}{"b" if beta else "."}{revision}'