#!/bin/bash
InterfaceAnalyzer.default.linuxgccdebug -database /home/rosetta/asa/rosetta_database  -fixedchains H L -out:file:scorefile $1.sc -in:file:s ./pdbdata/$1  @./code/rosetta_inputs/pack_input_options.txt
