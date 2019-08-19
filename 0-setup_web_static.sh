#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
if [[ ! -x /usr/sbin/nginx ]]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
PATH_TEST=/data/web_static/releases/test/
PATH_SHARED=/data/web_static/shared/
PATH_CURRENT=/data/web_static/current
FILE=index.html
mkdir -p $PATH_TEST $PATH_SHARED
echo "Cofigure the static web" | sudo tee "$PATH_TEST$FILE"
ln -snf $PATH_TEST $PATH_CURRENT
chown -R ubuntu:ubuntu /data
sed -i "56i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
service nginx restart
