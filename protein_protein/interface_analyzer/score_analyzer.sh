#!/bin/bash

score.default.linuxgccdebug -database /home/rosetta/asa/rosetta_database/ -s ./pdbdata/$1 -in:file:fullatom -ignore_unrecognized_res -out:file:scorefile ./$1.score
