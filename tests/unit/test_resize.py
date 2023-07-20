#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing resize implementation"""
import argparse
from os import path
from unittest import mock
from tests.base import BaseTest
from tests.base import Capturing
from imagepills.pills import Resize


class TestResizeWithErrorsBase(BaseTest):  # pragma: no cover
    """Common task to override check results method"""

    def check_results(self):
        """Method overriden to handle exception"""
        pass

    def test_launch(self):
        """Base method for launching a test

        base_class and arguments have to be initialized in to the child.
        """
        if self.test_class:
            with Capturing() as self.output_results:
                # Testing method run
                self.test_class.run()


class TestFileResizeBadWidth(TestResizeWithErrorsBase):
    """Tests file resize functionality with errors"""

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""
        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_resize",
                "-f",
                path.join(self.execution_path, "fixtures/image.png"),
                "-o",
                path.join(self.execution_path, self.output_folder),
                "-w",
                "123",
                "-e",
                "300",
                "-v",
            ],
        ):
            try:
                # Initialize test main class
                self.test_class = Resize("resize pill")
            except SystemExit as exc:
                self.assertIsInstance(exc.__context__, argparse.ArgumentError)


class TestFileResizeBadHeight(TestResizeWithErrorsBase):
    """Tests file resize functionality with errors"""

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""
        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_resize",
                "-f",
                path.join(self.execution_path, "fixtures/image.png"),
                "-o",
                path.join(self.execution_path, self.output_folder),
                "-w",
                "400",
                "-e",
                "234",
                "-v",
            ],
        ):
            try:
                # Initialize test main class
                self.test_class = Resize("resize pill")
            except SystemExit as exc:
                self.assertIsInstance(exc.__context__, argparse.ArgumentError)


class TestFileResizeInvalidWidth(TestResizeWithErrorsBase):
    """Tests file resize functionality with errors"""

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""
        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_resize",
                "-f",
                path.join(self.execution_path, "fixtures/image.png"),
                "-o",
                path.join(self.execution_path, self.output_folder),
                "-w",
                "asd1",
                "-e",
                "400",
                "-v",
            ],
        ):
            try:
                # Initialize test main class
                self.test_class = Resize("resize pill")
            except SystemExit as exc:
                self.assertIsInstance(exc.__context__, argparse.ArgumentError)


class TestFileResizeInvalidHeigth(TestResizeWithErrorsBase):
    """Tests file resize functionality with errors"""

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""
        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_resize",
                "-f",
                path.join(self.execution_path, "fixtures/image.png"),
                "-o",
                path.join(self.execution_path, self.output_folder),
                "-w",
                "400",
                "-e",
                "jh123df",
                "-v",
            ],
        ):
            try:
                # Initialize test main class
                self.test_class = Resize("resize pill")
            except SystemExit as exc:
                self.assertIsInstance(exc.__context__, argparse.ArgumentError)


class TestFileResizeWithHeight(BaseTest):
    """Tests file resize funtionalty"""

    # Results initialization
    expected_result = [{"success": [], "errors": []}]

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""
        # File path initialization
        file_path = path.join(self.execution_path, "fixtures", "image2.png")

        # Update expected results with file path
        self.expected_result[0]["success"] = [
            path.join(self.execution_path, "fixtures", "image2_497x500.png")
        ]

        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_resize",
                "-f",
                file_path,
                "-o",
                path.join(self.execution_path, self.output_folder),
                "-w",
                "300",
                "-e",
                "500",
                "-v",
            ],
        ):
            # Initialize test main class
            self.test_class = Resize("resize pill")

    def test_launch(self):
        """Base method for launching a test

        base_class and arguments have to be initialized in to the child.
        """
        if self.test_class:
            with Capturing() as self.output_results:
                # Testing method run
                self.test_class.run()


class TestFileResizeWithWidth(BaseTest):
    """Tests file resize funtionalty"""

    # Results initialization
    expected_result = [{"success": [], "errors": []}]

    def init_with_mock(self):
        """Method called by the parent to initialize class mocked"""
        # File path initialization
        file_path = path.join(self.execution_path, "fixtures", "image2.png")

        # Update expected results with file path
        self.expected_result[0]["success"] = [
            path.join(self.execution_path, "fixtures", "image2_400x402.png")
        ]

        # Mock arguments for size
        with mock.patch(
            "sys.argv",
            [
                "pills_resize",
                "-f",
                file_path,
                "-o",
                path.join(self.execution_path, self.output_folder),
                "-w",
                "400",
                "-e",
                "300",
                "-v",
            ],
        ):
            # Initialize test main class
            self.test_class = Resize("resize pill")

    def test_launch(self):
        """Base method for launching a test

        base_class and arguments have to be initialized in to the child.
        """
        if self.test_class:
            with Capturing() as self.output_results:
                # Testing method run
                self.test_class.run()
