#! /bin/sh

echo "make folder for pipe"
mkdir /run/shm/web
chown www-data:www-data /run/shm/web

chown www-data:www-data /tmp/testpipe
