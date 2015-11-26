#!/bin/bash
cd `pwd`

file='*'
[ "$(ls $1$file 2>/dev/null)" ]&&rm $1$file||echo "no such file like begin with $1"
cd ./interface_analyzer

#find ./  -name $1$file -ok rm -rf {} \;
[ "$(ls $1$file 2>/dev/null)" ]&&rm $1$file||echo "no such file like begin with $1"
cd ./pdbdata/
[ "$(ls $1$file 2>/dev/null)" ]&&rm $1$file||echo "no such file like begin with $1"
echo "remove the same file is done"

