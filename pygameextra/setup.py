# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pygameextra', 'pygameextra.tests']

package_data = \
{'': ['*'],
 'pygameextra': ['System Volume Information/*',
                 'build/scripts-3.8/*',
                 'dist/*',
                 'examples/pong/*',
                 'examples/tester/*',
                 'files/*',
                 'pygameextra_pong.egg-info/*',
                 'pygameextra_tester.egg-info/*'],
 'pygameextra.tests': ['testing_assets/*']}

install_requires = \
['pygame>=1.9.6', 'requests>=2.22.0']

setup_kwargs = {
    'name': 'pygameextra',
    'version': '1.6.5.2',
    'description': 'pygame extra is a mask for pygame, you can easily make complex games and or apps with much less lines then you would of before, Pygame Extra makes coding easier. The online documentation can be found at: https://pygame-extra.readthedocs.io/en/latest/',
    'long_description': None,
    'author': 'RedstoneHair',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
