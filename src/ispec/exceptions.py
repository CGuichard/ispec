"""Exceptions package of ispec."""

from ._types import Class, Method


class LocatedValidationError(Exception):
    """Generic validation error located inside python code.

    Error meant to be used to fail validation of python declarations, such
    as classes or methods. Provided location must give enough information
    to figure out the definition that could not be validated.
    """

    def __init__(self, module: str, name: str, reason: str) -> None:
        super().__init__(f"\n\n{module}.{name}: {reason}")
        self.module = module
        self.name = name
        self.reason = reason


class MethodValidationError(LocatedValidationError):
    """Validation error for method declaration."""

    def __init__(self, method: Method, reason: str) -> None:
        super().__init__(
            module=method.__module__,
            name=method.__qualname__,
            reason=reason,
        )
        self.method = method


class ClassValidationError(LocatedValidationError):
    """Validation error for class declaration."""

    def __init__(self, cls: Class, reason: str) -> None:
        super().__init__(
            module=cls.__module__,
            name=cls.__qualname__,
            reason=reason,
        )
        self.cls = cls
