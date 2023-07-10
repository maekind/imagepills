#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This file contains the base classes for testing"""
from os import path, mkdir, rmdir, getcwd
from unittest import TestCase
from io import StringIO
import sys


class TestExecutionInfo():
    """Class to provide exetuction information"""

    def __init__(self) -> None:
        """Default constructor"""

    @property
    def execution_path(self):
        """execution path property"""
        return path.split(path.abspath(__file__))[0]

    @property
    def working_directory(self):
        """working directory property"""
        return getcwd()


class Capturing(list):
    """Class for capturing stdout from a method"""

    # Class variables initialization
    _stdout = None
    _stringio = None

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class BaseTest(TestCase, TestExecutionInfo):
    """Base class for tests"""

    expected_result = []
    output_folder = 'output'
    output_results = None
    test_class = None

    def setUp(self) -> None:
        """Pre configuration for tests"""

        # Create output folder if it does not exist
        if not path.exists(self.output_folder):
            mkdir(self.output_folder)

        # Child class initialization (method defined in the children)
        self.init_with_mock()

        return super().setUp()

    def check_results(self, results):
        """Method to check results"""

        # Check same lenght
        self.assertEqual(len(results), len(self.expected_result))

        # Has to be lists
        self.assertIsInstance(self.expected_result, list)
        self.assertIsInstance(results, list)

        # We sort the results once
        sorted_results = sorted(results)
        sorted_expected_results = sorted(self.expected_result)

        # Compare results
        for index, result in enumerate(sorted_results):
            self.assertDictEqual(result, sorted_expected_results[index])

        print(f'Expected results: {sorted_expected_results}')
        print(f'Results: {sorted_results}')

    def tearDown(self) -> None:
        """Post configuration for tests"""
        # Clean
        if path.exists(self.output_folder):
            rmdir(self.output_folder)

        return super().tearDown()

    def init_with_mock(self):
        """Test class initialization with mocked arguments
        
            This method should be overriden in the child.
        """
