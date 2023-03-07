"""Types package of ispec.

Contains handy type definitions.
"""

from collections.abc import Callable
from typing import Any

__all__ = ["AnyCallable", "Class", "Method"]

Class = type[object]

AnyCallable = Callable[..., Any]
Method = AnyCallable
