from setuptools import setup
from os import path
import os

here = path.abspath(path.dirname(__file__))

setup(
    name='CoNIFER',
    version='0.2.2',
    description='python3 fork of github/nkrumm/CoNIFER',
    url='https://github.com/aseyboldt/CoNIFER',
    packages=['conifer'],
    license='GPL3',
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'tables',
        'pandas',
        'pysam',
    ],
    data_files={
        'probe_files': [os.listdir(path.join(here, 'probe_files'))]
    },
    entry_points={
        'console_scripts': [
            'conifer=conifer:main',
        ]
    }
)
