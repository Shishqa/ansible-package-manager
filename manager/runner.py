import os
import sys
import json
import subprocess


playbook_path = 'main.yml'
do_verbose = False


def set_verbose(value):
    do_verbose = value


def make_vars(host_pkg, state):
    vars = {}
    vars['input'] = {}
    vars['input']['pkg_list'] = host_pkg
    vars['input']['pkg_state'] = state
    return vars


def run(host_pkg, state):
    vars = make_vars(host_pkg, state)
   
    err = sys.stderr
    out = sys.stdout

    if (do_verbose):
        devnull = open(os.devnull, 'w')
        err = devnull
        out = devnull

    status = subprocess.run([
        "ansible-playbook", playbook_path,
        "--extra-vars", json.dumps(vars)
    ], stdout=out, stderr=err)

    if (do_verbose):
        devnull.close()

    return status.returncode
