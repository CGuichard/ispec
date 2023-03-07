# -*- coding: utf-8 -*-
"""Unit test package for `ispec._inspect`."""

import inspect

from ispec._inspect import get_methods, get_signature


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
