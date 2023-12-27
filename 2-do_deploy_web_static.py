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


    try:
        if not os.path.exists(archive_path):
            return False

        # Sending the archive to '/tmp/'
        put(archive_path, '/tmp/')

        # Extracting the file name without extension and repetitive dirs
        archive_name = os.path.basename(archive_path).split(".")[0]
        ddir = "/data/web_static/releases"

        # Creation of needed directories
        run("mkdir -p {}/{}/".format(ddir, archive_name))

        # Extracting the archive
        run("tar -xzf /tmp/{1}.tgz -C {0}/{1}/".format(ddir, archive_name))

        # Deletion of archive
        run("rm /tmp/{}.tgz".format(archive_name))

        # Moving contents of uncompressed archive to required dir
        run("mv {0}/{1}/web_static/* {0}/{1}/".format(ddir, archive_name))

        # Deleting previously extracted files
        run("rm -rf {}/{}/web_static".format(ddir, archive_name))

        # Removing old symbolic link
        run("rm -rf /data/web_static/current")

        # Creating new symbolic link
        run("ln -s {}/{}/ /data/web_static/current".format(ddir, archive_name))

        # Optional printing
        print("New version deployed!")
    except Exception:
        return False
