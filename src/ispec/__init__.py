"""Top-level package for ispec."""

from importlib.metadata import PackageNotFoundError, version

from .decorators import abstractclass, ispec, typehint

try:
    __version__ = version("ispec")
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    __version__ = "undefined"
