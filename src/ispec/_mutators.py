"""Mutators package of ispec.

Module containing functions used to mutate methods
and classes.
"""

from abc import abstractmethod
from typing import cast

from ._inspect import get_methods, is_abstract, is_bound
from ._types import Class, Metaclass, Method


def add_metaclass(cls: Class, metaclass: Metaclass) -> Class:
    """Dynamically add metaclass to class.

    ..note: From six library, six.add_metaclass decorator
    """
    cls_dict = cls.__dict__.copy()
    cls_slots = cls_dict.get("__slots__")
    if cls_slots is not None:
        for slot_var in cls_slots:
            cls_dict.pop(slot_var)
    cls_dict.pop("__dict__", None)
    cls_dict.pop("__weakref__", None)
    cls_dict["__qualname__"] = cls.__qualname__

    return metaclass(cls.__name__, cls.__bases__, cls_dict)


def set_methods_abstract(cls: Class) -> None:
    """Apply abc.abstractmethod to the methods of a class.

    This function make the direct methods of a
    class abstract. It means that if class B
    inherit class A, using this function on
    class B will only set abstract the methods
    declared in class B.
    """
    for method in get_methods(cls):
        if not is_abstract(method):
            abstract_method = make_method_abstract(method)
            setattr(cls, method.__name__, abstract_method)


def make_method_abstract(method: Method) -> Method:
    """Return given method after applying abc.abstractmethod."""
    if is_bound(method):
        # Bound method means @classmethod,
        # but if we directly apply abstractmethod() on it
        # the order will be wrong and an error would be
        # thrown because bound methods are read-only.
        # We need to "repack" the method while applying
        # the decorators in the good order.
        origin_method = cast(Method, getattr(method, "__func__", method))
        abstract_method = abstractmethod(origin_method)
        _method = cast(Method, classmethod(abstract_method))
    else:
        _method = abstractmethod(method)
    return _method
