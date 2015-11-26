import os
from setuptools import setup

install_requires = ['matplotlib', 'numpy', 'pandas']

try:
    with open('README.rst') as readme:
        long_description = readme.read()
except IOError:
    long_description = 'See https://pypi.python.org/pypi/calmap'

# This is quite the hack, but we don't want to import our package from here
# since that's recipe for disaster (it might have some uninstalled
# dependencies, or we might import another already installed version).
distmeta = {}
for line in open(os.path.join('calmap', '__init__.py')):
    try:
        field, value = (x.strip() for x in line.split('='))
    except ValueError:
        continue
    if field == '__version_info__':
        value = value.strip('[]()')
        value = '.'.join(x.strip(' \'"') for x in value.split(','))
    else:
        value = value.strip('\'"')
    distmeta[field] = value

setup(
    name='calmap',
    version=distmeta['__version_info__'],
    description='Calendar heatmaps from Pandas time series data',
    long_description=long_description,
    author=distmeta['__author__'],
    author_email=distmeta['__contact__'],
    url=distmeta['__homepage__'],
    license='MIT License',
    platforms=['any'],
    packages=['calmap'],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering']
)
