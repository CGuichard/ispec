"""Basic package test."""


def test_package_import():
    import ispec  # noqa


def test_package_version_is_defined():
    import ispec

    assert ispec.__version__ != "undefined"
