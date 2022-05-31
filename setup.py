# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in silent_print/__init__.py
from silent_print import __version__ as version

setup(
	name='silent_print',
	version=version,
	description='Silent print using https://github.com/imTigger/webapp-hardware-bridge',
	author='Roque Vera',
	author_email='roquegv@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
