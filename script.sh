#!/bin/sh
python process.py
git add -A
git commit -m "updated data"
git push origin master
