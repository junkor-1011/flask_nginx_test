#!/usr/bin/env bash
# https://qiita.com/A-Kira/items/3339e902e7a8fca8fdf6

psql -U puser -d postgre < "/docker-entrypoint-initdb.d/create-tables.sql"
psql -U puser -d postgre < "/docker-entrypoint-initdb.d/insert-data.sql"

