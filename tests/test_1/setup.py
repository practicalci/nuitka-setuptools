import os
import sys
from setuptools import setup

os.chdir(os.path.dirname(__file__) or '.')

packages = ['package1']

if any('bdist' in arg for arg in sys.argv):
    from nuitka_setuptools import Nuitka, Compile

    build_settings = dict(
        # Compile module
        cmdclass={'build_ext': Nuitka},
        ext_modules=Compile(packages, False, ['--show-scons','--file-reference-choice', 'original']),
    )
else:
    build_settings = {}

setup(
    name='nuitka_setuptools_test_1',
    py_modules=[],
    packages=['package1'],
    description='Test packages build for nuitka_setuptools',
    author='Mario Costa',
    author_email='mario.silva.costa@gmail.com',
    url='https://github.com/mjscosta/nuitka_testcases',
    version="0.1",
    include_package_data=True,
    package_data={'': ['*.so', '*.pyd'] }, # include pre-compiled native libs
    zip_safe=False,
    **build_settings
)
