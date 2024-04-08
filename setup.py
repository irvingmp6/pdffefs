from setuptools import find_packages, setup
from _version import __version__

setup(
    name='pdffefs',
    version=__version__,
    author = "Irving Martinez",
    packages=find_packages(),
    install_requires =[
        'Pillow==7.0.0',
        'PyPDF4==1.27.0',
    ],
    entry_points = {
        'console_scripts': [
            'pdffefs = src.__main__:main',
        ]
    }
)