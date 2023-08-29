VERSION = '2.0.0'
revision = 10
alpha = False
beta = True
release_candidate = False


def get():
    return f'{VERSION}{"b" if beta else "a" if alpha else "rc" if release_candidate else ""}{revision}'
