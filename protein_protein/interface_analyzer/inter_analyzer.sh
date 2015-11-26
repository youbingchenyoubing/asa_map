#!/bin/bash
InterfaceAnalyzer.default.linuxgccdebug -database /home/rosetta/asa/rosetta_database  -out:file:scorefile $1.sc -in:file:s ./pdbdata/$1   @./code/pack_input_options.txt
