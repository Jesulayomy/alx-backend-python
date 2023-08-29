#!/usr/bin/env python3
""" Unittests for the utils.access_nested_map method """

import unittest
from parameterized import parameterized
from typing import (
    Any,
    Dict,
    Mapping,
    Sequence,
)
from unittest.mock import (
    Mock,
    patch,
)
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """ The Main class for Access Nested Map func"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """ Test that the method returns the expected results """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected: Any) -> None:
        """ Test that a KeyError is raised for error cases """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


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

    def test_memoize(self) -> None:
        """ Tests tthe memoize(d) methods and wrapper """
        class TestClass:
            """ A simple  testing class """
            def a_method(self) -> int:
                """ A simple tester method """
                return 42

            @memoize
            def a_property(self) -> int:
                """ A simple property method """
                return self.a_method()

        with patch.object(TestClass, "a_method") as amd:
            myClass = TestClass()
            myClass.a_property
            myClass.a_property
            amd.assert_called_once
            self.assertEqual(myClass.a_property, amd.return_value)
