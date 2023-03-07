# -*- coding: utf-8 -*-
"""Unit test package for `ispec._validators`."""


from typing import Optional

import pytest

from ispec._validators import (
    ClassValidationError,
    MethodValidationError,
    validate_class_typehint,
    validate_method_typehint,
)


class TestValidateMethodTypehint:
    def test_missing_return_annotation_raise_error(self):
        def dummy_method(self):
            pass

        with pytest.raises(MethodValidationError):
            validate_method_typehint(dummy_method)

    def test_self_do_not_need_annotation(self):
        def dummy_method(self) -> None:
            pass

        validate_method_typehint(dummy_method)

    def test_cls_do_not_need_annotation(self):
        def dummy_classmethod(cls) -> None:
            pass

        validate_method_typehint(dummy_classmethod)

    def test_staticmethod_do_not_need_first_arg(self):
        def dummy_staticmethod() -> None:
            pass

        validate_method_typehint(dummy_staticmethod)

    def test_staticmethod_first_arg_is_validated(self):
        def dummy_staticmethod(a) -> None:
            pass

        with pytest.raises(MethodValidationError):
            validate_method_typehint(dummy_staticmethod)

    def test_method_with_multiple_param_missing_an_annotation(self):
        def dummy_method(a: int, b, c: Optional[bool] = None) -> int:
            pass

        with pytest.raises(MethodValidationError):
            validate_method_typehint(dummy_method)

    def test_method_with_multiple_param_missing_an_annotation_2(self):
        def dummy_method(a: int, b: str, c=None) -> int:
            pass

        with pytest.raises(MethodValidationError):
            validate_method_typehint(dummy_method)

    def test_method_with_multiple_param(self):
        def dummy_method(a: int, b: str, c: Optional[bool] = None) -> int:
            pass

        validate_method_typehint(dummy_method)


class TestValidateClassTypehint:
    def test_class_with_invalid_method(self):
        class A:
            def dummy(self, a):
                pass

        with pytest.raises(ClassValidationError):
            validate_class_typehint(A)

    def test_class_with_valid_method_and_invalid_method(self):
        class A:
            def dummy(self, a: int) -> int:
                pass

            def dummy2(self, a: int):
                pass

        with pytest.raises(ClassValidationError):
            validate_class_typehint(A)

    def test_class_with_valid_method(self):
        class A:
            def dummy(self, a: int) -> int:
                pass

        validate_class_typehint(A)
