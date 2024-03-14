#!/usr/bin/env python3
""" Duck-typed annotations """
from typing import Any, Union, Sequence, Iterable, List, Tuple


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ First element retrieved"""
    if lst:
        return lst[0]
    else:
        return None
