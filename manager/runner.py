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
    status = subprocess.run([
        "ansible-playbook", playbook_path,
        "--extra-vars", json.dumps(vars),
        "--limit", ":".join(list(vars['input']['pkg_list'].keys()))
    ])

    return (status.returncode == 0)
