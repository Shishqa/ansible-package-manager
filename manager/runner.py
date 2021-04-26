import os
import sys
import json
import subprocess


playbook_path = 'playbook.yml'


def make_vars(host_pkg, state):
    vars = {}
    vars['input'] = {}
    vars['input']['pkg_list'] = host_pkg
    vars['input']['pkg_state'] = state
    return vars


def run(host_pkg, state):
    vars = make_vars(host_pkg, state)
    
    devnull = open(os.devnull, 'w')

    status = subprocess.run([
        "ansible-playbook", playbook_path,
        "--extra-vars", json.dumps(vars)
    ], stdout=devnull, stderr=devnull)

    devnull.close()

    return status.returncode
