#!/bin/bash
str=""
splitString="${2}"
OLD_IFS="$IFS"
IFS=":"
arr=($splitString)
IFS="$OLD_IFS"
for s in ${arr[@]}
do
str+=$s' '
done
InterfaceAnalyzer.default.linuxgccdebug -database /home/rosetta/asa/rosetta_database -fixedchains $str  -out:file:scorefile $1.sc -in:file:s ./pdbdata/$1  @./code/pack_input_options.txt 
