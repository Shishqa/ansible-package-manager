import sys
from . import parser
from . import runner
from . import reader as rd


def uninstall_pkg(host_pkg):
    print('UNINSTALLING: ', end='')
    sys.stdout.flush()
    status = runner.run(host_pkg, "absent")
    if status != 0:
        print('FAILED')
    else:
        print('OK')
    return status


def install_pkg(host_pkg):
    print('INSTALLING: ', end='')
    sys.stdout.flush()
    status = runner.run(host_pkg, "present")
    if status != 0:
        print('FAILED, RUNNING ROLLBACK')
        uninstall_pkg(host_pkg)
    else:
        print('OK')
    return status


def manage_pkg(lines, uninstall, verbose):
    reader = rd.Reader(lines)
    host_pkg = parser.parse(reader)
    runner.set_verbose(verbose)
    if uninstall:
        return uninstall_pkg(host_pkg)
    else:
        return install_pkg(host_pkg)
