from setuptools import setup, find_packages
import codecs
import os

VERSION = '2.0.0b0'
short = 'Pygame. Made easier'
long = '''Pygame Extra is a mask for pygame, 
you can easily make complex games and or apps with much less lines then you would of before, 
Pygame Extra makes coding easier. 

The online documentation can be found at: https://pygame-extra.readthedocs.io/en/latest/

github: https://github.com/JustRedTTG/PGE'''

# Setting up
setup(
    name="pygameextra",
    version=VERSION,
    author="Red",
    author_email="redtonehair@gmail.com",
    description=short,
    long_description_content_type="text/markdown",
    long_description=long,
    packages=['pygameextra'],
    install_requires=['pygame'],
    package_data={'pygameextra': ['font.ttf']
    },
    keywords=['python'],
    classifiers=[
       "Development Status :: 1 - Planning",
       "Intended Audience :: Developers",
       "Programming Language :: Python :: 3",
       "Operating System :: Unix",
       "Operating System :: MacOS :: MacOS X",
       "Operating System :: Microsoft :: Windows",
   ]
)
