# setup.py
from setuptools import setup, find_packages

setup(
    name="serial_assistant",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'PySide6',
        'transitions',
        'pykka',
        'rxpy',
        'pyserial',
    ],
    entry_points={
        'console_scripts': [
            'serial_assistant=src.main:main',
        ],
    },
)
