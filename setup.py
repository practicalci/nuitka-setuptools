import os
import sys
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

install_requires = ['nuitka>=0.6<0.7', ]

PY2 = sys.version_info[0] == 2
if PY2:
    install_requires.append('pathlib2')


setup(
    name='nuitka_setuptools',
    version='0.6.0',
    py_modules=['nuitka_setuptools'],
    description='Extension to setuptools to run your package through nuitka to '
                'produce compiled, faster, obfuscated binary modules.',
    long_description=long_description,
    author='Andrew Leech',
    author_email='andrew@alelec.net',
    url='https://github.com/practicalci/nuitka-setuptools',
    include_package_data=True,
    install_requires=install_requires,
)
