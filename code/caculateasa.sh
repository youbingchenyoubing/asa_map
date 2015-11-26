#!/bin/bash
#usage ./caculateasa.py {uncomplex} {complex} {outfile}
cd /home/rosetta/asa
python caculateasa.py -o1 $1 -o2 $2 -o3 $3
