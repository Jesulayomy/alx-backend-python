#!/usr/bin/env python3
""" type-annotated function to_kv function """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ changes  a  string to keys and value """

    return (k, v * v)
