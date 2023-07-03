"""Top-level module for ispec."""

from importlib.metadata import PackageNotFoundError, version

from .decorators import abstractclass, ispec, typehint

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    __version__ = "undefined"
