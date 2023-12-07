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
        file_name = archive_path.split('/')[-1]
        w_file_name = file_name.split('.')[0]
        r_path = f'/data/web_static/releases/{w_file_name}/'
        tmp_path = f'/tmp/{file_name}'
        print(r_path)
        print(tmp_path)
        put(archive_path, '/tmp/')
        run(f'mkdir -p {r_path}')
        run(f'tar -xzf {tmp_path} -C {r_path}')
        run(f'rm {tmp_path}')
        run(f"mv {r_path}web_static/* {r_path}")
        run(f"rm -rf {r_path}web_static")
        run('rm -rf /data/web_static/current')
        run(f'ln -s {r_path} /data/web_static/current')
        print("New version deployed!")
        return True
    except Exception:
        return False
