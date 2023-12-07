#!/usr/bin/python3
"""archive module"""
from fabric.api import env
from fabric.api import run
from fabric.api import put
import os


def do_deploy(archive_path):
    """archive files web_static"""
    env.user = 'ubuntu'
    env.hosts = ['100.24.238.196', '23.23.74.47']
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = path.split('/')[-1]
        put(archive_path, f'/tmp/{file_name}')
        run(f'tar -xzvf /tmp/{file_name} -C /data/web_static/releases/')
        run(f'rm /tmp/{file_name}')
        run('rm -f /data/web_static/current')
        run('ln -s /data/web_static/releases/ /data/web_static/current')
        return True
    except Exception:
        return False
