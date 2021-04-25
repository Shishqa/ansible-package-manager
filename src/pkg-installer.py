#!/bin/python

#============================================================================#

import sys
import os
import json
import argparse

#============================================================================#

def parse_input(reader):
    host_packages = {}

    hosts = []
    apt_packages = []
    pip_packages = []
        
    for line in reader:
        line_split = line.rstrip().split(' ')
        if len(line_split) == 0:
            continue
        elif line_split[0] == 'apt':
            apt_packages = line_split[1:]
            print(apt_packages)
        elif line_split[0] == 'pip':
            pip_packages = line_split[1:]
            print(pip_packages)

            for host in hosts:
                host_packages[host] = {}
                host_packages[host]['apt'] = apt_packages[:]
                host_packages[host]['pip'] = pip_packages[:]
                print(host_packages)
           
            hosts.clear()
            apt_packages.clear()
            pip_packages.clear()

        else:
            hosts.append(line_split[0])
            print(hosts)

    return host_packages

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def run_ansible(host_packages, state):
    config = {}
    config['host_packages'] = host_packages
    config['state'] = state

    pid = os.fork()
    if pid == 0:
        os.execlp("ansible-playbook", "ansible-playbook",
                  "main.yml",
                  "--extra-vars", json.dumps(config),
                  "--limit", ":".join(list(config['host_packages'].keys())))
    else:
        pid, sts = os.waitpid(pid, 0)
        return (sts == 0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def print_usage():
    print(f"""{'-'*80}
{ sys.argv[0] } - install multiple packages to multiple hosts
using Ansible as a backend
    
usage: { sys.argv[0] } [file-with-packages]
{'-'*80}""")


def get_reader(path):
    with open(path, 'r') as pkg_data:
        lines = pkg_data.readlines()
        return iter(lines)


def main():
    if len(sys.argv) != 2:
        print_usage()
        exit(1)
    
    reader = get_reader(sys.argv[1])
    vars = parse_input(reader)

    if run_ansible(vars, "present"):
        print("OK")
    else:
        run_ansible(vars, "absent")
        print("FAIL")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

if __name__ == '__main__':
    main()

#============================================================================#
