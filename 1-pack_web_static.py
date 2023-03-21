#!/usr/bin/python3
'''Fabric script'''

from fabric.api import *
from datetime import datetime


def do_pack():
    '''do pack module'''

    file_name = "web_static_" + \
        datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    save_dir = "versions/"

    local("mkdir -p " + save_dir)
    chk = local("tar -cvzf {}{} web_static".format(save_dir, file_name))
    if chk.succeeded:
        return (save_dir + file_name)
    else:
        return (None)
