# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pygameextra']

package_data = \
{'': ['*']}

install_requires = \
['pygame>=1.9.6,<2.0.0']

setup_kwargs = {
    'name': 'pygameextra',
    'version': '1.6.3',
    'description': 'pygame extra is a mask for pygame, you can easily make complex games and or apps with much less lines then you would of before, Pygame Extra makes coding easier',
    'long_description': None,
    'author': 'RedstoneHair',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
