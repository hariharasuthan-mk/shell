#!/bin/sh

# This is a comment, too!
path=${1}
commandOutput=$(python /python/list-files-directories-recursively.py ${1})
echo "Output was =>$commandOutput"
