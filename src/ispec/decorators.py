"""Decorators package of ispec.

Module containing the decorators, the
core functionalities of the library.
"""

from abc import ABCMeta

from ._mutators import add_metaclass, set_methods_abstract
from ._types import Class
from ._validators import validate_class_typehint


def typehint(cls: Class) -> Class:
    """Class decorator that check if the decorated class is correctly type hinted."""
    validate_class_typehint(cls)
    return cls


def abstractclass(cls: Class) -> Class:
    """Class decorator that make a decorated class abstract."""
    set_methods_abstract(cls)
    return add_metaclass(cls, ABCMeta)
