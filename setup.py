import re

from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pynmcli',
	version=get_version('pynmcli/__init__.py'),
	description='Simple python interface to Network Manager CLI',
	long_description=readme(),
	license='MIT',
	author='Federico Barresi',
	author_email='fede.barresi@gmail.com',
	url='https://github.com/fbarresi/PyNmcli',
	packages=find_packages(exclude=['tests']),
	include_package_data=True,
    install_requires=[
        'setuptools',
    ],
)