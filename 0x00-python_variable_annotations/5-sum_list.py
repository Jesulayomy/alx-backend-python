#!/usr/binenv python3
""" A type annotated function using  sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Collects a list of floats and returns the sum of all list elements """

    return sum(input_list)
