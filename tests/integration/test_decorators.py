# -*- coding: utf-8 -*-
"""Integration test package for `ispec.decorators`."""

from unittest.mock import MagicMock, patch


class TestISpecDecorator:
    @patch("ispec.decorators.typehint")
    def test_ispec_use_typehint(self, mock_typehint: MagicMock):
        mock_typehint.side_effect = lambda cls: cls

        from ispec.decorators import ispec

        @ispec
        class A:
            pass

        assert (
            mock_typehint.called
        ), "The ispec decorator should call the typehint decorator"

    @patch("ispec.decorators.abstractclass")
    def test_ispec_use_abstractclass(self, mock_abstractclass: MagicMock):
        mock_abstractclass.side_effect = lambda cls: cls

        from ispec.decorators import ispec

        @ispec
        class A:
            pass

        assert (
            mock_abstractclass.called
        ), "The ispec decorator should call the abstractclass decorator"
