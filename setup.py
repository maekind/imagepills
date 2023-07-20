#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python packageing entry point."""

from setuptools import setup
from pkg_resources import parse_requirements

# Read the requirements from the requirements.txt file
with open("requirements.txt") as requirements_file:
    requirements = [str(req) for req in parse_requirements(requirements_file)]


setup(
    name="imagepills",
    version="1.0",
    packages=["imagepills"],
    author="Marco Espinosa",
    author_email="marco@marcoespinosa.es",
    description="image pills package",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "pills_size = imagepills.imagepills:size",
            "pills_image2png = imagepills.imagepills:image2png",
            "pills_resize = imagepills.imagepills:resize",
        ]
    },
    install_requires=requirements,
)
