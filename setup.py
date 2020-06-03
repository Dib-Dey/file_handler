from setuptools import setup

__version__ = "1.0.0"

setup(
    name = 'pypo',
    version = __version__,
    packages = ['pycli'],
    entry_points = {
        'console_scripts': [
            'pypo = pypo.__main__:main'
        ]
    })