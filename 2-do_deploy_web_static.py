#!/usr/bin/python3
"""archive module"""
from fabric.api import *
from datetime import datetime
import os


def do_pack(archive_path):
    """archive files web_static"""
    env.user = 'ubuntu'
    env.hosts = ['100.24.238.196', '23.23.74.47']
    if not os.path.exists(archive_path):
        return False
    try:
        local('mkdir -p versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        arc_filename = f'web_static_{date}.tgz'
        arc_str = f'tar -czvf versions/{arc_filename} web_static'
        local(arc_str)
        put('versions/' + arc_filename, '/tmp/' + arc_filename)
        run(f'tar -xzvf /tmp/{arc_filename} -C /data/web_static/releases/')
        run(f'rm /tmp/{arc_filename}')
        c.run('rm -f /data/web_static/current')
        c.run('ln -s /data/web_static/releases/ /data/web_static/current')
        return True
    except Exception:
        return False
