#!/bin/sh

cd /home/tospaa/python/ozerlastikdjango
gunicorn --workers 1 --bind unix:/tmp/gunicorn.sock tsp_prj.wsgi

