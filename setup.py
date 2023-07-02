#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python packageing entry point."""

from setuptools import setup
from pkg_resources import parse_requirements

# Read the requirements from the requirements.txt file
with open('requirements.txt') as requirements_file:
    requirements = [str(req) for req in parse_requirements(requirements_file)]


setup(
    name='imagepils',
    version='1.0',
    packages=['imagepils'],
    author = 'Marco Espinosa',
    author_email = 'marco@marcoespinosa.es',
    description = 'image pils package',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Environment :: Console',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'pils_size = imagepils.imagepils:size',
            'pils_image2png = imagepils.imagepils:image2png',
            'pils_resize = imagepils.imagepils:resize',
        ]
    },
    install_requires=requirements,
)
