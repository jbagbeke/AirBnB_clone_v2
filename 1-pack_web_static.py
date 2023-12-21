#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generates .tgz archive from contents of web_static folder

        Returns:
            str: The path to generated archive on success, else None
    """

    local("mkdir -p versions")

    time_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    arch_name = "versions/web_static_{}.tgz".format(time_str)

    result = local("tar -cvzf {} web_static".format(arch_name))

    if result.succeeded:
        return arch_name
    else:
        return None
