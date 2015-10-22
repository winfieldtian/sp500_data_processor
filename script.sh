#!/bin/sh
python process_test.py
git add -A
git commit -m "updated data"
git push origin master
