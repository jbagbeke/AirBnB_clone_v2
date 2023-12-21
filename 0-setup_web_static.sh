#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

index="\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$index" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/server_name _;/a\ \n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}" /etc/nginx/sites-available/default

sudo service nginx restart
