"""Validators package of ispec.

Module containing functions used to validate methods
and classes definitions.
"""

from collections.abc import ValuesView
from inspect import Parameter

from ._inspect import get_methods, get_signature
from ._types import Class, Method
from .exceptions import ClassValidationError, MethodValidationError


def validate_class_typehint(cls: Class) -> None:
    """Validate class type hinting.

    :raises ClassValidationError: error raised if one method or more in the
                                  given class raises a
                                  :class:`~ispec.validators.MethodValidationError`.
    """
    validations_errors: list[MethodValidationError] = []
    for method in get_methods(cls):
        try:
            validate_method_typehint(method)
        except MethodValidationError as err:
            validations_errors.append(err)
    if validations_errors:
        reason = "could not validate class\n" + "".join(
            f"- {e.name}: {e.reason}\n" for e in validations_errors
        )
        raise ClassValidationError(cls, reason=reason)


def validate_method_typehint(method: Method) -> None:
    """Validate the method type hinting.

    :raises MethodValidationError: error raised if type annotations are missing
                                   for the method return, or in the method parameters.
    """
    signature = get_signature(method)

    missing_annotations: list[str] = []

    if signature.return_annotation == signature.empty:
        missing_annotations.append("method return")

    if params := signature.parameters.values():
        _inspect_params_annotations(params, missing_annotations)

    if missing_annotations:
        missing_str = (
            ", ".join(missing_annotations[:-1])
            + (" and " if len(missing_annotations) > 1 else "")
            + missing_annotations[-1]
        )
        raise MethodValidationError(method, f"missing annotation for {missing_str}")


def _inspect_params_annotations(
    params: ValuesView[Parameter],
    missing_annotations: list[str],
) -> None:
    first, *others = params

    if first.name not in ["self", "cls"] and first.annotation == first.empty:
        missing_annotations.append(f"parameter {first.name}")

    for param in others:
        if param.annotation == param.empty:
            missing_annotations.append(f"parameter {param.name}")
