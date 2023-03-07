"""Decorators package of ispec.

Module containing the decorators, the
core functionalities of the library.
"""

from ._types import Class
from ._validators import validate_class_typehint


def typehint(cls: Class) -> Class:
    """Class decorator that check if the decorated class is correctly type hinted."""
    validate_class_typehint(cls)
    return cls
