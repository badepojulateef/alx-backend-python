#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code
and apply any necessary changes.

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
"""
from typing import List


def zoom_array(lst: List, factor: int = 2) -> List:
    """
    Zooms in on the elements of a list by repeating
    each element a specified number of times.

    Args:
        lst (List): The input list.
        factor (int, optional): The zoom factor, which
        determines how many times each element isrepeated. Defaults to 2.

    Returns:
        List: A new list containing each element of the
        input list repeated according to the zoom factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
