import os
import prody

def removeTERFunction(pdbfile):
    pdb=prody.parsePDB(pdbfile)
    itername=pdb.getFlagLabels()
    print "itername is : %s" % itername
    #for i in xrange(0,len(pdb)):
    pdb.delData('pdbter')


def removeTER2(pdb):
    print 'begin remove pdb Ter'
    import shutil
    pdbfile=os.getcwd()+'/interface_analyzer/pdbdata/'+pdb
    f=open(pdbfile)
    g=open(pdbfile+'_new','w')
    for line in f.readlines():
        if 'ATOM' in line and 'TER' not in line:
            g.write(line)
    f.close()
    g.close()
    shutil.move(pdbfile+'_new',pdbfile) 


'''
def main():
    import argparse
    
    parser=argparse.ArgumentParser()
    parser.add_argument('-f', action='store', required=True, dest='pdbfile',
                    help='PDB file of protein-protein complex')
    inputs=parser.parse_args()
    

    pdbfile1=os.getcwd()+'/interface_analyzer/pdbdata/'+inputs.pdbfile
    removeTER2(pdbfile1)


if __name__=="__main__":
    print "in main"
    main()
    ''' 
