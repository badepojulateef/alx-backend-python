#!/usr/bin/env python3
"""
Given the parameters and the return values, add
type annotations to the function

Hint: look into TypeVar


def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""

from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,\
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary, returning
    the value if the key exists, or the default value if not.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up in the dictionary.
        default (Optional[T]): The default value to return if the
        key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key in the
        dictionary, or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
