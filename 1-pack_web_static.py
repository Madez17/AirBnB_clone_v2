#!/usr/bin/python3
# script that generates a .tgz archive from the contents of the web_static
from fabric.api import local


def do_pack():
    local("mkdir -p versions")
    compressed = local("tar -czvf \"versions/web_static_\
                       $(date '+%Y%m%d%H%M%S').tgz\" web_static")

    if (compressed.succeeded):
        return local("echo \"versions/web_static_\
                     $(date '+%Y%m%d%H%M%S').tgz\"")
    else:
        return None
