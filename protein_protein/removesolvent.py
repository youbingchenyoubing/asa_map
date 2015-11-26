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

def removesolvent(pdbfile):
    dirname=os.getcwd()+'/interface_analyzer/pdbdata/'+pdbfile
    pdbfileselect=pdbfile.split('.')
    print "remove solvent for pdb"
    pymol.finish_launching()
    pymol.cmd.load(dirname)
    pymol.cmd.remove('solvent')
    pymol.cmd.select('target',pdbfileselect[0])
    pymol.cmd.save(dirname,(('target')))
    pymol.cmd.delete('all')
    pymol.cmd.quit()
    print "remove solvent done"
