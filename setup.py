from setuptools import setup

version = "2.0.0b49"
short = 'Pygame. Made easier.'
long = '''Pygame Extra is an extension for pygame, 
you can easily make complex games and or apps with much less code then you would otherwise, 
Pygame Extra is a engine for creating complex interactions without the need for making everything yourself 

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
    install_requires=['pygame', 'numpy', 'frozendict'],
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
