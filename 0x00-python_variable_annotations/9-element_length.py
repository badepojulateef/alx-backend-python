#!/usr/bin/env python3
"""
Annotate the below function’s parameters and
return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in the input
    list and returns a list of tuples.

    Each tuple contains:
    - The original element from the input list.
    - The length of the element.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each
        tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
