#!/usr/bin/env python3
""" Unittests for the utils.access_nested_map method """

from parameterized import parameterized
from typing import List, Dict, Any, Mapping, Sequence
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ The Main class for Access Nested Map func"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nest: Mapping, path: Sequence, res: Any):
        """ tests the mappig using assert statements """
        self.assertEqual(access_nested_map(nest, path), res)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nest: Mapping, path: Sequence):
        """ Tests that the parameters raise a KeyError exception """
        with self.assertRaises(KeyError):
            access_nested_map((nest, path))


class TestGetJson(unittest.TestCase):
    """ tests the get_json method of the utils module """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """ Tests the get json method form utils module """

        kwargs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**kwargs)) as req:
            res = get_json(test_url)
            self.assertEqual(res, test_payload)
            req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Tests the memoize function using unittests """

    def test_memoize(self):
        """ Tests tthe memoize(d) methods and wrapper """
        class TestClass:
            """ A simple  testing class """
            def a_method(self):
                """ A simple tester method """
                return 42

            @memoize
            def a_property(self):
                """ A simple property method """
                return self.a_method()

        with patch(TestClass, "a_method", ret=lambda: 42) as amd:
            my_object = TestClass()
            self.assertEqual(my_object.a_property(), 42)
            self.assertEqual(my_object.a_property(), 42)
            amd.assert_called_once()
