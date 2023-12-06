#!/usr/bin/python3
"""archive module"""
from fabric.api import local, Connection, run
from datetime import datetime
import os


def do_pack(archive_path):
    """archive files web_static"""
    user = 'ubuntu'
    servers = ['100.24.238.196', '23.23.74.47']
    if os.path.exists(archive_path):
        local('mkdir -p versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        arc_filename = f'web_static_{date}.tgz'
        arc_str = f'tar -czvf versions/{arc_filename} web_static'
        local(arc_str)
        for server in servers:
            c = Connection(host=f'{user}@{server}')
            c.put('versions/' + arc_filename, '/tmp/' + arc_filename)
            c.run(f'tar -xzvf /tmp/{arc_filename} \
                    -C /data/web_static/releases/')
            c.run(f'rm /tmp/{arc_filename}')
            c.run('rm -f /data/web_static/current')
            c.run('ln -s /data/web_static/releases/* /data/web_static/current')
    else:
        return False
