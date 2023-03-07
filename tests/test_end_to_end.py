"""End-to-end package test."""

import pytest

from ispec import ispec
from ispec.exceptions import ClassValidationError


def test_ispec():
    @ispec
    class MyInterface:
        def method_dummy(self, a: str) -> str:
            ...

        @staticmethod
        def static_method_dummy(b: str) -> str:
            ...

        @classmethod
        def class_method_dummy(cls, c: str) -> str:
            ...

    class A(MyInterface):
        def method_dummy(self, a: str) -> str:
            print(f"method {a=}")

        @staticmethod
        def static_method_dummy(b: str) -> str:
            print(f"static method {b=}")

        @classmethod
        def class_method_dummy(cls, c: str) -> str:
            print(f"class method {c=}")

    with pytest.raises(TypeError) as excinfo:
        MyInterface()

    assert "Can't instantiate abstract class" in str(excinfo.value)

    mi: MyInterface = A()


def test_ispec_missing_methods():
    @ispec
    class MyInterface:
        def method_dummy(self, a: str) -> str:
            ...

        @staticmethod
        def static_method_dummy(b: str) -> str:
            ...

        @classmethod
        def class_method_dummy(cls, c: str) -> str:
            ...

    class B(MyInterface):
        pass

    with pytest.raises(TypeError) as excinfo:
        B()

    assert "Can't instantiate abstract class" in str(excinfo.value)
    assert "with abstract method" in str(excinfo.value)
    for m in ["method_dummy", "static_method_dummy", "class_method_dummy"]:
        assert m in str(excinfo.value)


def test_ispec_typehint():
    with pytest.raises(ClassValidationError) as excinfo:

        @ispec
        class MyInterface:
            def method_dummy(self, a: str):
                ...

            @staticmethod
            def static_method_dummy(b) -> str:
                ...

            @classmethod
            def class_method_dummy(cls, c):
                ...

    assert "MyInterface: could not validate class" in str(excinfo.value)
    assert "method_dummy: missing annotation for method return" in str(excinfo.value)
    assert "static_method_dummy: missing annotation for parameter b" in str(
        excinfo.value
    )
    assert (
        "class_method_dummy: missing annotation for method return and parameter c"
        in str(excinfo.value)
    )
