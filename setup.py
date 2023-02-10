from setuptools import setup, find_packages
from pyleaf import __version__

extra_test = [
    'pytest>=4',
    'pytest-cov>=2',
]

extra_dev = [
    *extra_test,
]


setup(
    name='pyleaf',
    description='*******************',

    url='https://github.com/robertpettis/pyleaf.git',
    author='Robert Pettis',
    author_email='pettisrobert@gmail.com',

    packages=find_packages(),
    
    install_requires = [
        'geojson',
        'pandas',
        'geopandas'
    ],
    extras_require={
        'dev': extra_dev,
        'test':extra_test,
    },
    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
