#!/bin/bash
cd /home/rosetta/asa/protein_protein/interface_analyzer/pdbdata
python mutate_model.py $1 $2 'ALA' $3
