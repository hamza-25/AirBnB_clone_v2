#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt update
sudo apt install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
content_html="
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
</head>
<body>
    <p>hello world!</p>
</body>
</html>
"
echo "$content_html" > /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu /data/
sudo sed -i '/root \/var\/www\/html;/a\ \ \ \ location \/hbnb_static {\n \ \ \ \ \ \ alias \/data\/web_static\/current\/;\n \ \ \ \ }' /etc/nginx/sites-available/default
