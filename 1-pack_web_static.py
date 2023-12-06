#!/usr/bin/python3
""" """
from fabric.api import run
from datetime import datetime
def do_pack():
    """ """
    run('mkdir -p versions')
    date = str(datetime.now().strftime("%Y%m%d%H%M%S")) + '.tgz'
    arc_str = f"tar -czvf {date} web_static"
    move_file = f"mv ./{date} ./versions"
    run(arc_str)
    run(move_file)
do_pack()
