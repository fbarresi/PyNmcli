from setuptools import setup, find_packages


the_version = open("VERSION").read().strip()

setup(name='PyNmcli',
	version=the_version,
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