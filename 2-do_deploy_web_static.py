#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder.
"""


from fabric.api import run, put, env
import os


env.hosts = ['52.91.168.145', '54.236.17.91']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """

    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')

        arch_name = archive_path.split('/')[-1].replace('.tgz', '')
        path = '/data/web_static/releases/' + arch_name
        arch_path = '/tmp/' + arch_name + '.tgz'

        run("mkdir -p {}".format(path))
        run("tar -xzf {} -C {}".format(arch_path, path))
        run("rm {}".format(arch_path))
        run("mv {}/web_static/* {}/".format(path, path))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))

        return True
    else:
        return False
