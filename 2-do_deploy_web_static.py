#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder.
"""


from fabric.api import run, put, env
import os


env.hosts = ['52.91.168.145', '54.236.17.91']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """

    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')

        arch_name = archive_path.split('/')[-1].replace('.tgz', '')
        
        ddir = '/data/web_static/releases/' + arch_name
        
        arch_path = '/tmp/' + arch_name + '.tgz'

        run("sudo mkdir -p {}".format(ddir))

        run("sudo tar -xzf /tmp/{}.tgz -C {}".format(arch_name, ddir))

        run("sudo sudo rm -rf /tmp/{}.tgz".format(arch_name))

        run("sudo mv {}/web_static/* {}".format(ddir, ddir))

        run("sudo rm -rf {}/web_static".format(ddir))

        run("sudo rm -rf /data/web_static/current")

        run("sudo ln -s {}/ /data/web_static/current".format(ddir))

        return True
    else:
        return False
