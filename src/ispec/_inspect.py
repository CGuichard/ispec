"""Inspect package of ispec.

Module containing functions used to inspect
methods and classes.
"""

import inspect

from ._types import AnyCallable, Class, Method


def get_signature(obj: AnyCallable) -> inspect.Signature:
    """Encapsulate inspect.signature."""
    return inspect.signature(obj)


def get_methods(cls: Class) -> list[Method]:
    """Return the list of the methods declared in a class."""
    return [
        method
        for method_name, method in (
            inspect.getmembers(cls, predicate=inspect.isfunction)
            + inspect.getmembers(cls, predicate=inspect.ismethod)
        )
        if method_name in cls.__dict__
    ]
