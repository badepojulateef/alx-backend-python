#!/usr/bin/env python3
"""
A type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the floats in the input list.
    """
    return float(sum(input_list))
