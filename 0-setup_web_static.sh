#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "hello world!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
}" > /etc/nginx/sites-available/default
sudo service nginx restart
