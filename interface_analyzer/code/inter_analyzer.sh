#!/bin/bash
InterfaceAnalyzer.default.linuxgccdebug -database /home/rosetta/asa/rosetta_database -fixedchains H L -out:file:scorefile $1.sc -in:file:s $1
