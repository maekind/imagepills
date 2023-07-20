#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing size implementation"""
from os import path
from unittest import mock
from tests.base import BaseTest
from tests.base import Capturing
from imagepills.pills import Size


class TestWithoutArguments(BaseTest):
    """Tests file size functionality without arguments"""

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""
        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_size"
            ],
        ):
            # Initialize test main class
            self.test_class = Size("size pill")

    def check_results(self):
        """Method overriden to handle exception"""
        pass

    def test_launch(self):
        """Base method for launching a test

            base_class and arguments have to be initialized in to the child.        
        """
        if self.test_class:
            with Capturing() as self.output_results:
                try:
                    # Testing method run
                    self.test_class.run()
                except SystemExit as exc:
                    self.assertEqual(exc.code, 99)


class TestFileSize(BaseTest):
    """Tests file size functionality"""

    # Results initialization
    expected_result = [
        {'filename': 'image.png', 'width': 2127, 'height': 2127}
    ]

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""
        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_size",
                "-f",
                path.join(self.execution_path, "fixtures/image.png"),
                "-v"
            ],
        ):
            # Initialize test main class
            self.test_class = Size("size pill")

    def test_launch(self):
        """Base method for launching a test

            base_class and arguments have to be initialized in to the child.        
        """
        if self.test_class:
            with Capturing() as self.output_results:
                # Testing method run
                self.test_class.run()


class TestFilesInFolderSize(BaseTest):
    """Tests files size in foldel"""

    # Results initialization
    expected_result = [
        {'filename': 'image.png', 'width': 2127, 'height': 2127},
        {'filename': 'image2.png', 'width': 500, 'height': 503},
        {'filename': 'sample.jpg', 'width': 300, 'height': 300},
    ]

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""
        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_size",
                "-i",
                path.join(self.execution_path, "fixtures"),
                "-v"
            ],
        ):
            # Initialize test main class
            self.test_class = Size("size pill")

    def test_launch(self):
        """Base method for launching a test

            base_class and arguments have to be initialized in to the child.        
        """
        if self.test_class:
            with Capturing() as self.output_results:
                # Testing method run
                self.test_class.run()
