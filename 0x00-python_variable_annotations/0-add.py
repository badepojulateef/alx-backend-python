#!/usr/bin/env python3
"""
A type-annotated function add that takes a float a and a
float b as arguments and returns their sum as a float
"""


def add(a: float, b: float) -> float:
    """
    Add two floating-point numbers and return the result.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        float: The sum of `a` and `b`.

    Example:
        >>> add(1.11, 2.22)
        3.33
    """
    return a + b
