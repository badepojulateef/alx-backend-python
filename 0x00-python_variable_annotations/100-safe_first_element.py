#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""
from typing import Sequence, Union


 def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence): The input sequence.

    Returns:
        Union[None, lst[0]]: The first element of the sequence or None
        if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
