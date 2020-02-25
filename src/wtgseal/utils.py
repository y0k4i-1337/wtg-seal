"""Utilities for wtg-seal.

This module offers utilities function for wtg-seal, mainly focused on file
parsing.

"""

from typing import List, TextIO

WebObject = List[int]


def parse_objects(file: TextIO) -> List[WebObject]:
    objs = [[int(x) for x in l.split()] for l in file.readlines()]
    return objs
