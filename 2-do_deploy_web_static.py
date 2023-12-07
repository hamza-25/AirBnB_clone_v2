#!/usr/bin/python3
"""archive module"""
from fabric.api import env
from fabric.api import run
from fabric.api import put
import os


env.hosts = ['100.24.238.196', '23.23.74.47']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """archive files web_static"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = path.split('/')[-1]
        w_file_name = file_name.split('.')[0]
        put(archive_path, '/tmp/')
        run(f'mkdir -p /data/web_static/releases/{w_file_name}/')
        run(f'tar -xzvf /tmp/{file_name} \
                -C /data/web_static/releases/{w_file_name}/')
        run(f'rm /tmp/{file_name}')
        run('rm -f /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{w_file_name}/ \
                /data/web_static/current')
        print("New version deployed!")
        return True
    except Exception:
        return False
