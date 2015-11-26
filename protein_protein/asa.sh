#!/bin/bash
#usage ./asa.sh {pdbfilename} {outfile1} {outfile_sum}
cd `pwd` 
python asa_np.py -f $1 -o $2 -s 2000 -o1 $3 
