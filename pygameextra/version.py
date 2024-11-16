VERSION = '2.0.0'
revision = 2
alpha = False
beta = False
release_candidate = True


def get():
    return f'{VERSION}{"b" if beta else "a" if alpha else "rc" if release_candidate else "."}{revision}'
