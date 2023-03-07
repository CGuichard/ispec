"""Types package of ispec.

Contains handy type definitions.
"""

from collections.abc import Callable
from typing import Any

__all__ = ["AnyCallable", "Class", "Metaclass", "Method"]

Class = type[object]
Metaclass = type[type]

AnyCallable = Callable[..., Any]
Method = AnyCallable
