#!/usr/bin/python3
# script that generates a .tgz archive from the contents of the web_static
from fabric.api import local
from os import path

env.hosts = ['104.196.157.169', '34.73.109.46']
env.user = "ubuntu"


def do_pack():
    local("mkdir -p versions")
    compressed = local("tar -czvf \"versions/web_static_\
                       $(date '+%Y%m%d%H%M%S').tgz\" web_static")

    if (compressed.succeeded):
        return local("echo \"versions/web_static_\
                     $(date '+%Y%m%d%H%M%S').tgz\"")
    else:
        return None

def do_deploy(archive_path):
    
    if path.exists("archive_path") is True:
        put(archive_path, "/tmp/")
        filename_uncompress = archive_path.split("/")[1].split(".")[0]
        run("tar -xvzf /tmp/filename_uncompress /data/web_static/releases/")
        run("rm /tmp/archive_path")
        run("rm /data/web_static/current")
        run("ln -snf /data/web_static/current  /data/web_static/releases/filename_uncompress")
        return True
    else:
        return False
