#!/usr/bin/python3

import sys
import argparse
from manager import manager


def get_argparser():
    ap = argparse.ArgumentParser()
    ap.add_argument("pkg_file", type=str,
                    help="path of file with packages and hosts")
    ap.add_argument("-u", "--uninstall", action="store_true",
                    help="uninstall packages listed in file \
                        (installing by default)")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="print ansible logs to stdout")
    return ap


def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()


def main():
    argparser = get_argparser()
    args = argparser.parse_args()
    try:
        lines = read_lines(args.pkg_file)
    except IOError:
        print('[Error]: cannot open {}'.format(args.pkg_file))
        argparser.print_usage()
        exit(1)

    status = manager.manage_pkg(lines, args.uninstall, args.verbose)
    exit(status)


if __name__ == '__main__':
    main()
