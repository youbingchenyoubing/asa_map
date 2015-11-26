import sys
import os
import __main__
__main__.pymol_argv=['pymol','-rqkc']
try :
    import pymol
    del pymol
except ImportError :
    print "pymol has not been installed on this system.Please install it from the following link:"
    print "http://www.pymol.org/"
    sys.exit(1)
    pass
import pymol
from pymol import cmd,stored,math


def removechainHL(pdbfile):
    dirname=os.getcwd()+'/interface_analyzer/'+pdbfile
    pdbfileselect=pdbfile.split('.')
    savefile=os.getcwd()+'/interface_analyzer/'+pdbfileselect[0]+'_antigen.pdb'
    print "remove antibody of complex,so can caculate the value of antigen sasa "
    pymol.finish_launching()
    pymol.cmd.load(dirname)
    pymol.cmd.remove('hydrogens')
    pymol.cmd.remove('solvent')
    pymol.cmd.remove('chain L+H')
    pymol.cmd.select('target',pdbfileselect[0])
    pymol.cmd.save(savefile,(('target')))
    pymol.cmd.delete('all')
    pymol.cmd.quit()
    print "remove the antibody of complex have done"
    return savefile

def renamechain(pdbfile,chainbefore,chainafter):
    dirname=os.getcwd()+'/interface_analyzer/'+pdbfile
    pdbfileselect=pdbfile.split('.')
    print "rename the chain name of pdb i order to make antibody'chain is H ro L"
    pymol.finish_launching()
    pymol.cmd.load(dirname)
    pymol.cmd.alter((chainbefore),chain=chainafter)
    pymol.cmd.save(dirname,((pdbfileselect[0]))) 
    pymol.cmd.delete('all')
    pymol.cmd.quit()
    print "rename name of chain has been done"
    


