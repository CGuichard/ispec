# -*- coding: utf-8 -*-
"""Unit test package for `ispec._inspect`."""

import inspect
from abc import abstractmethod

from ispec._inspect import get_methods, get_signature, is_abstract, is_bound


class TestIsBound:
    def test_method_is_not_bound(self):
        class A:
            def dummy(self):
                pass

        assert not is_bound(A.dummy)

    def test_staticmethod_is_not_bound(self):
        class A:
            @staticmethod
            def dummy():
                pass

        assert not is_bound(A.dummy)

    def test_classmethod_is_bound(self):
        class A:
            @classmethod
            def dummy(cls):
                pass

        assert is_bound(A.dummy)


class TestIsAbstract:
    def test_method_is_not_abstract(self):
        class A:
            def dummy(self):
                pass

        assert not is_abstract(A.dummy)

    def test_abstractmethod_is_abstract(self):
        class A:
            @abstractmethod
            def dummy(self):
                pass

        assert is_abstract(A.dummy)


def test_get_signature_return_signature():
    def dummy():
        pass

    signature = get_signature(dummy)
    assert isinstance(signature, inspect.Signature)


class TestGetMethods:
    def test_use(self):
        class A:
            def dummy(self):
                pass

            def another_dummy(self):
                pass

        methods = get_methods(A)
        assert A.dummy in methods
        assert A.another_dummy in methods

    def test_do_not_give_parent_methods(self):
        class A:
            def dummy(self):
                pass

        class B(A):
            def another_dummy(self):
                pass

        assert A.dummy not in get_methods(B)
