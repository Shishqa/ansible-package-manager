import sys
import argparse
import parser
import runner


def get_argparser():
    ap = argparse.ArgumentParser()
    ap.add_argument("pkg_file", type=str,
                    help="path of file with packages and hosts")
    ap.add_argument("-u", "--uninstall", action="store_true",
                    help="uninstall packages listed in file \
                        (installing by default)")
    return ap


def uninstall_pkg(host_pkg):
    print('UNINSTALLING: ', end='')
    sys.stdout.flush()
    status = runner.run(host_pkg, "absent")
    if not status:
        print('FAILED')
    else:
        print('OK')


def install_pkg(host_pkg):
    print('INSTALLING: ', end='')
    sys.stdout.flush()
    status = runner.run(host_pkg, "present")
    if not status:
        print('FAILED')
        uninstall_pkg(host_pkg)
    else:
        print('OK')


def main():
    argparser = get_argparser()
    args = argparser.parse_args()
    host_pkg = parser.parse(args.pkg_file)
    if args.uninstall:
        uninstall_pkg(host_pkg)
    else:
        install_pkg(host_pkg)


if __name__ == '__main__':
    main()
