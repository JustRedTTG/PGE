VERSION = '2.0.0'
revision = 5
beta = True


def get():
    return f'{VERSION}{"b" if beta else "."}{revision}'
