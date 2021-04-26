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
        print('FAILED')
        uninstall_pkg(host_pkg)
    else:
        print('OK')
    return status


def main():
    argparser = get_argparser()
    args = argparser.parse_args()
    try:
        host_pkg = parser.parse(args.pkg_file)
    except IOError:
        print('[Error]: cannot open {}'.format(args.pkg_file))
        argparser.print_usage()
        exit(1)

    if args.uninstall:
        status = uninstall_pkg(host_pkg)
    else:
        status = install_pkg(host_pkg)
    exit(status)


if __name__ == '__main__':
    main()
