#!/bin/sh
# https://qiita.com/A-Kira/items/3339e902e7a8fca8fdf6
docker-compose exec db bash -c "chmod 0775 docker-entrypoint-initdb.d/init-database.sh"
docker-compose exec db bash -c "./docker-entrypoint-initdb.d/init-database.sh"
