#!/bin/sh
python process.py
git add -A
git commit -m "updating data for this week"
git push origin master
