from setuptools import setup, find_packages
print('===setup PGE===')
setup(
    name='pygameextra-pong',
    packages=find_packages(include=['scripts/pygameextra-pong,pygameextra-pong,bin/*']),
    scripts=['examples/pong/pygameextra-pong']
)
