#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This file contains the base classes for testing"""
from os import path, mkdir, rmdir, getcwd, remove
from unittest import TestCase
from io import StringIO
import shutil
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
    fixtures_folder = 'fixtures'
    output_folder = 'output'
    output_results = None
    test_class = None

    def setUp(self) -> None:
        """Pre configuration for tests"""

        # Create output folder if it does not exist
        if not path.exists(path.join(self.execution_path, self.output_folder)):
            mkdir(path.join(self.execution_path, self.output_folder))

        # Child class initialization (method defined in the children)
        self.init_with_mock()

        return super().setUp()

    def check_results(self):
        """Method to check results"""

        # Search for list of results. Other items should be message errors.
        for output in self.output_results:
            try:
                output_results = eval(output)
                if isinstance(output_results, list):
                    break
            except SyntaxError:
                continue

        # Check for results type.
        self.assertIsInstance(output_results, list)

        # Check same lenght
        self.assertEqual(len(output_results), len(self.expected_result))

        # Check same list
        self.assertListEqual(output_results, self.expected_result)

        # Prepare the output and print results
        #  TODO: Maybe only print when assertion fails
        output = {
            'Expected results': self.expected_result,
            'Results': output_results,
        }

        print(f'Output: {output}')

    def tearDown(self) -> None:
        """Post configuration for tests"""
        #  Cleanning: Delete output folder
        if path.exists(path.join(self.execution_path, self.output_folder)):
            shutil.rmtree(path.join(self.execution_path, self.output_folder))

        # Checking results
        self.check_results()

        return super().tearDown()

    def init_with_mock(self):
        """Test class initialization with mocked arguments
        
            This method should be overriden in the child.
        """
