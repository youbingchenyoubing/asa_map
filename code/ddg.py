#!/usr/bin/env python
import os
import sys
import argparse
import linecache


def beginmutate(pdbfile,position,chain):
    os.system('./mutateresidues.sh '+pdbfile+' '+position+' '+chain)
    print "have mutate %s.pdb chain %s %s done " % (pdbfile, chain,position)

def getmutatelist(file_dist,file_asa,pdbfile):
    import getmutateresidue
    from getmutateresidue import getmutateresidues
    return getmutateresidues(file_asa,file_dist,pdbfile) 
     

def caculatemethod1(line1,line):
    print "waiting caculate of %s ddg" % line1
    os.system('./interface.sh '+line1)
    dirname=os.getcwd()
    dirname+='/interface_analyzer/'+line1+'.sc'
    print "dirname:%s "% dirname 
    theline=linecache.getline(dirname,3)
    theline=theline.strip('\n')
    theline=theline.split(' ',1000)
    for i in theline:
        if i=='':
            theline.remove(i)
    dirname=os.getcwd()+'/interface_analyzer/'+line.split('.')[0]+'_sc.txt'
    f_file=open(dirname,'r+')
    f_file.read()
    f_file.write(line1+':'+theline[5]+'\n')
    f_file.close()
    print "caculte done with %s ddg" % line1


def caculateasa(pdbfile,n=0):
    if n==0:
        result=pdbfile+'_complexasa'
    else:
        result=pdbfile+'_antigenasa'
    processresult=pdbfile+'_processasa'
    os.system('./asa.sh '+pdbfile+' '+processresult+' '+result)


def removeantibody(pdbfile):
    import removeantibody
    from removeantibody import removechainHL
    removechainHL(pdbfile)


def caculatecomplexandantigen(pdbfile,pdbfile1):
    path=os.getcwd()
    file1=path+'/interface_analyzer/'+pdbfile+'_complexasa'
    file2=path+'/interface_analyzer/'+pdbfile1+'_antigenasa'
    file3=path+'/interface_analyzer/'+pdbfile.split('.')[0]+'_asa' 
    os.system('./caculateasa.sh'+' '+file2+' '+file1+' '+file3)
    print 'the result have been stored in %s'% file3
    return file3


def caculatedistance(pdbfile):
    path=os.getcwd()
    n=4.0
    filename=path+'/interface_analyzer/'+pdbfile+'_distance'+str(n)
    os.system('./pairwise.sh '+pdbfile)
    print 'the result of distance have been stored in %s'% filename
    return filename

def main():
    parser=argparse.ArgumentParser() 
    parser.add_argument('-path', action='store', required=True, dest='pathfile',
                    help='pathfile is a textfile of name of pdb')
    inputs=parser.parse_args()
    pathfile=inputs.pathfile
    file_pathfile=open(pathfile)
    for line in file_pathfile: # caculate the value of ddg before mutation
        line=line.strip('\n') 
        print "caulate of %s ddg" % line
        os.system('./interface.sh '+line)
        dirname=os.getcwd()
        dirname+='/interface_analyzer/'+line+'.sc'
        theline=linecache.getline(dirname,3)
        theline=theline.strip('\n')
        thelinesplit=theline.split(' ',1000)
        for i in thelinesplit:
            if i=='':
                thelinesplit.remove(i) 
        dirname=os.getcwd()+'/interface_analyzer/'+line.split('.')[0]+'_sc.txt'
        f_file=open(dirname,'w')
        f_file.write(line+':'+thelinesplit[5]+'\n')
        f_file.close()
    file_pathfile.close()
    file_pathfile=open(pathfile)
    for line in file_pathfile:
        line=line.strip('\n')
        pdbfileselect=line.split('.')
        removeantibody(line)
        pdbantigenfile=pdbfileselect[0]+'_antigen.pdb'
        caculateasa(line,0)
        caculateasa(pdbantigenfile,1)
        file1=caculatecomplexandantigen(line,pdbantigenfile)
        print "*************the asa caculation have done****************"
        file2=caculatedistance(line)
        print "*******the distance of 4.0 caculation have done*********"
        mutatelistfile=getmutatelist(file2,file1,line)
        print"*************************%sbegin mutate************" % line
        f_mutate=open(mutatelistfile)
        for linemutate in f_mutate:
            linemutate=linemutate.strip('\n')
            linemutatesplit=linemutate.split(':')
            print "mutate chain %s %s" % (linemutatesplit[0],linemutatesplit[1])
            beginmutate(pdbfileselect[0],linemutatesplit[1],linemutatesplit[0])
            aftermutatefile=pdbfileselect[0]+'ALA'+linemutatesplit[1]+'.pdb'
            caculatemethod1(aftermutatefile,line)
        f_mutate.close()
    file_pathfile.close()
    print "the program caculate over"
    
if __name__=="__main__":
    print "in main"
    main()
