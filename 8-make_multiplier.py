#!/usr/bin/env python3
""" type-annotated function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a mulltiplier function """

    return lambda x: x * multiplier
