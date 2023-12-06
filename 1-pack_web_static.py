#!/usr/bin/python3
"""archive module"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """archive files web_static"""
    local('mkdir -p versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    arc_filename = f'versions/web_static_{date}.tgz'
    arc_str = f'tar -czvf {arc_filename} web_static'
    local(arc_str)
