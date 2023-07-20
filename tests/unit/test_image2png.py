#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing size implementation"""
from os import path
from unittest import mock
from tests.base import BaseTest
from tests.base import Capturing
from imagepills.pills import Convert2PNG


class Image2PngTestBase():
    """Base class with common info"""

    def test_launch(self):
        """Base method for launching a test

            base_class and arguments have to be initialized in to the child.        
        """
        if self.test_class:
            with Capturing() as self.output_results:
                # Testing method run
                self.test_class.run()


class TestFileConversion(Image2PngTestBase, BaseTest):
    """Tests file conversion functionality"""

    # Results initialization
    expected_result = [
        {'success': [], 'errors': []}
    ]

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""

        # File path initialization
        file_path = path.join(self.execution_path, "fixtures/sample.jpg")

        # Update expected results with file path
        self.expected_result[0]['success'] = [file_path]

        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_image2png",
                "-f",
                file_path,
                "-o",
                path.join(self.execution_path, self.output_folder),
                "-v"
            ],
        ):
            # Initialize test main class
            self.test_class = Convert2PNG("convert to png pill")

class TestFilesInFolderConversion(Image2PngTestBase, BaseTest):
    """Tests file conversion functionality"""

    # Results initialization
    expected_result = [
        {'success': [], 'errors': []}
    ]

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""

        # File path initialization
        file_path = path.join(self.execution_path, "fixtures")

        # Update expected results with file path
        self.expected_result[0]['success'] = ['image.png', 'image2.png', 'sample.jpg']
        self.expected_result[0]['errors'] = ['non_image.jpg']

        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_image2png",
                "-i",
                file_path,
                "-o",
                path.join(self.execution_path, self.output_folder),
                "-v"
            ],
        ):
            # Initialize test main class
            self.test_class = Convert2PNG("convert to png pill")


class TestNonImageFileConversion(Image2PngTestBase, BaseTest):
    """Tests file conversion functionality"""

    # Results initialization
    expected_result = [
        {'success': [], 'errors': []}
    ]

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""

        # File path initialization
        file_path = path.join(self.execution_path, "fixtures/non_image.jpg")

        # Update expected results with file path
        self.expected_result[0]['errors'] = [file_path]

        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_image2png",
                "-f",
                file_path,
                "-o",
                path.join(self.execution_path, self.output_folder),
                "-v"
            ],
        ):
            # Initialize test main class
            self.test_class = Convert2PNG("convert to png pill")
