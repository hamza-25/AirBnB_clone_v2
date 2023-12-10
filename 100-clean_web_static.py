#!/usr/bin/python3
"""archive module
"""

from fabric.api import *

env.hosts = ['100.24.238.196', '23.23.74.47']
env.user = 'user'


def do_clean(number=0):
    """delete all unnecessary archive"""

    number = int(number)
    if number == 0 or number == 1:
        number = 2
    else:
        number = number + 1
    local(f'cd versions; ls -t | tail -n +{number} | xargs rm -rf')
    path = '/data/web_static/releases'
    run(f'cd {path}; ls -t | tail -n +{number} | xargs rm -rf')
