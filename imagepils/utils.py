#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Utils library module"""
import os

__author__ = "Marco Espinosa"
__email__ = "marco@marcoespinosa.es"
__date__ = "20/06/2023"
__version__ = "1.0"
__type__ = "module"

def walk(root) -> list:
    """Method to walk throught the given folder

        :param root: root folder

        :return: list of files
    """
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # yield every filename to updload
        for filename in filenames:
            #print(os.path.join(dirpath, filename))
            files.append(filename)
        # call the method recursively for the subfolders
        for dirname in dirnames:
            walk(os.path.join(dirpath, dirname))

    return files

def normalize_folder(folder) -> str:
    """Method that normalizes the folder

        Normalization:
            - Strip right / or \\
            - if a . is provided, it converts to the current path

        :param folder: string that contains a folder path.

        :return: normalized folder
    """
    _folder = folder.rstrip('\\/')

    return _folder if _folder != "." else os.getcwd()
