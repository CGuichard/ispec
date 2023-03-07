# -*- coding: utf-8 -*-
"""Unit test package for `ispec._mutators`."""


from unittest.mock import MagicMock, patch

from ispec._mutators import add_metaclass, make_method_abstract, set_methods_abstract


def test_add_metaclass():
    class Meta(type):
        pass

    class A:
        pass

    class B:
        __slots__ = "b"

    add_metaclass(A, Meta)
    add_metaclass(B, Meta)


@patch("ispec._mutators.make_method_abstract")
def test_set_methods_abstract(mock_make_method_abstract: MagicMock):
    from abc import abstractmethod

    mock_make_method_abstract.side_effect = lambda meth: meth

    class A:
        def dummy(self):
            pass

        @abstractmethod
        def another_dummy(self):
            pass

    mock_make_method_abstract.assert_not_called()
    set_methods_abstract(A)
    mock_make_method_abstract.assert_called_with(A.dummy)


def test_make_method_abstract():
    class A:
        def dummy(self):
            pass

        @staticmethod
        def static_dummy():
            pass

        @classmethod
        def classmethod_dummy(cls):
            pass

    assert not getattr(A.dummy, "__isabstractmethod__", False)
    assert not getattr(A.static_dummy, "__isabstractmethod__", False)
    assert not getattr(A.classmethod_dummy, "__isabstractmethod__", False)

    make_method_abstract(A.dummy)
    make_method_abstract(A.static_dummy)
    make_method_abstract(A.classmethod_dummy)

    assert getattr(A.dummy, "__isabstractmethod__", False)
    assert getattr(A.static_dummy, "__isabstractmethod__", False)
    assert getattr(A.classmethod_dummy, "__isabstractmethod__", False)
