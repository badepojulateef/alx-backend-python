#!/usr/bin/env python3
"""
A type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v
and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v and returns a tuple.

    The first element of the tuple is the string k.
    The second element is the square of the int/float v,
    annotated as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): An integer or a float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k and
        the square of v as a float.
    """
    return (k, float(v**2))
