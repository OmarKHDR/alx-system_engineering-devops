#!/usr/bin/env bash
if [$# -ne 1];then
    echo "usage: ./0-body_size.sh ip:port"
    exit 1
fi
url=$1
curl -s -X GET http://$1/ -H HTTP/1.0 -w "\n\n%{size_download}\n" | tail -n 1
