from setuptools import setup
from version import get as get_version

version = get_version()
short = 'Pygame. Made easier.'
long = '''Pygame Extra is a mask for pygame, 
you can easily make complex games and or apps with much less lines then you would of before, 
Pygame Extra makes coding easier. 

The online documentation can be found at: https://pygame-extra.readthedocs.io/en/latest/

github: https://github.com/JustRedTTG/PGE'''

# Setting up
setup(
    name="pygameextra",
    version=version,
    author="Red",
    author_email="redtonehair@gmail.com",
    description=short,
    long_description_content_type="text/markdown",
    long_description=long,
    packages=['pygameextra', 'pygameextra_tester'],
    install_requires=['pygame', 'numpy'],
    package_data={'pygameextra': ['font.ttf'], 'pygameextra_tester': [
        'columns.png', 'rows.png',
        'Xbutton.png', 'Ybutton.png',
        'mario_01.png',
        'debug_icon.png', 'mouse_middle.png'
    ]},
    keywords=['python'],
    entry_points={
        'console_scripts': [
            'pygameextra-tester = pygameextra_tester.__init__:run',
        ],
    }
)
