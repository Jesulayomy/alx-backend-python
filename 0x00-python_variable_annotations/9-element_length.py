#!/usr/bin/env python3
""" type-annotated function make_multiplier """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a mulltiplier function """

    return [(i, len(i)) for i in lst]
