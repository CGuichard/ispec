"""Top-level package for ispec."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("ispec")
except PackageNotFoundError:
    # package is not installed
    __version__ = "undefined"
