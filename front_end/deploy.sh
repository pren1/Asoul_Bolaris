#!/usr/bin/env bash
rm -r html
npm run build
mv dist html
scp -r html/ root@47.242.222.3://usr/share/nginx