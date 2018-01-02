import re

from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']

setup(name='PyNmcli',
	version=get_version('pynmcli/__init__.py'),
    platforms=['linux'],
	description='Simple python interface to Network Manager CLI',
	license='commercial license',
	author='Federico Barresi',
	author_email='fede.barresi@gmail.com',
	url='https://github.com/fbarresi/PyNmcli',
	packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[],
    include_package_data=True
)