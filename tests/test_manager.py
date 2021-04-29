import pytest
from context import manager


class TestJustWorks:
    def test_valid_install(self):
        input = [
            "192.168.10.10",
            "192.168.10.11",
            "apt nginx traceroute",
            "192.168.10.12",
            "pip numpy"
        ]
        status = manager.manage_pkg(input, uninstall=False, verbose=True)
        assert (status == 0)

    def test_valid_uninstall(self):
        input = [
            "192.168.10.10",
            "192.168.10.11",
            "apt nginx traceroute",
            "192.168.10.12",
            "pip numpy"
        ]
        status = manager.manage_pkg(input, uninstall=True, verbose=True)
        assert (status == 0)


def test_empty_input():
    input = []
    status = manager.manage_pkg(input, uninstall=False, verbose=True)
    assert (status == 0)


def test_invalid_host():
    input = [
        "123.123.123.123",
        "192.168.10.11",
        "apt nginx traceroute",
        "192.168.10.12",
        "pip numpy"
    ]
    status = manager.manage_pkg(input, uninstall=False, verbose=True)
    assert (status != 0)


def test_invalid_package():
    input = [
        "192.168.10.10",
        "192.168.10.11",
        "apt nginx traceroute",
        "192.168.10.12",
        "apt helloworld",
        "pip numpy"
    ]
    status = manager.manage_pkg(input, uninstall=False, verbose=True)
    assert (status != 0)
