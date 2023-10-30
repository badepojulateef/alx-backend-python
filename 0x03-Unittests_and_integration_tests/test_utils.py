#!/usr/bin/env python3
"""Familiarize yourself with the utils.access_nested_map function and
understand its purpose. Play with it in the Python console to make
sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for
ollowing inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
"""

import unittest
from unittest.mock import patch, MOCK
import utils


class TestAccessNestedMap(unittest.TestCase):
    """
    Test the access_nested_map function with various inputs.

    Args:
        nested_map (dict): The nested map to access.
        path (tuple): The path to navigate within the map.
        expected_output: The expected result of accessing the path.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test the access_nested_map function."""
        res = utils.access_nested_map(nested_map, path)
        self.assertEqual(res, expected_result)

        @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])

    def test_access_nested_map_exception(self, nested_map, path):
        """Test exception handling in access_nested_map function."""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
