VERSION = '2.0.0'
revision = 1
alpha = True
beta = False


def get():
    return f'{VERSION}{"b" if beta else "a" if alpha else "."}{revision}'
