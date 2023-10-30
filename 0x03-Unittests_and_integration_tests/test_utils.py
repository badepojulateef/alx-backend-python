#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function and
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
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test the access_nested_map function with various inputs.

    Args:
        nested_map (dict): The nested map to access.
        path (tuple): The path to navigate within the map.
        expected_output: The expected result of accessing the path.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),  # Test with a simple map and path
            ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Test with nested map and path
            ({"a": {"b": 2}}, ("a", "b"), 2),  # Test deeper nested map and path
        ]
    )
    def test_access_nested_map_success(self, nested_map, path, expected_output):
        """Test the access_nested_map function with various inputs.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path to navigate within the map.
            expected_output: The expected result of accessing the path.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

        @parameterized.expand(
        [
            ({}, ("a",), KeyError),  # Test with an empty map and path
            ({"a": 1}, ("a", "b"), KeyError),  # Test with missing path in the map
        ]
    )

    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """Test exception handling in access_nested_map function.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path to navigate within the map.
            expected_exception: The expected exception to be raised.
        """
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


    class TestGetJson(unittest.TestCase):
    """Test class for the get_json function."""

    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False}),
        ]
    )
    def test_get_json(self, url, expected_output):
        """Test the get_json function with different URLs.

        Args:
            url (str): The URL to request JSON data from.
            expected_output: The expected JSON response.
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expected_output)

class TestMemoize(unittest.TestCase):
    """Test class for the memoize decorator."""

    def test_memoize(self):
        """Test the memoize decorator.

        This test checks whether the @memoize decorator correctly caches the result
        of a method, ensuring that it is called only once and returns the cached value
        on subsequent calls.
        """
        class TestClass:
            """Test class for memoization."""
            def a_method(self):
                """A method for testing memoization."""
                return 42

            @memoize
            def a_property(self):
                """A memoized property using the memoize decorator."""
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
