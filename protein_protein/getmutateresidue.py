import os
import sys

def getmutateresidues(file_asa,file_distance,pdbfile):
    path=os.getcwd()
    pdbfileselect=(pdbfile.split('.'))[0]
    resultfile=path+'/interface_analyzer/'+pdbfileselect+'_mutate'
    f_result_mutate=open(resultfile,'w')
    f_distance=open(file_distance)
    lineNum=0;
    set1=set([])
    for line in f_distance:
        if lineNum!=0:
            line=line.strip('\n')
            linesplit=line.split('to')
            linesplitagain=linesplit[0].split('/',4)
            '''if linesplitagain[2]!='ALA' and linesplitagain[2]!='GLY':
                string=linesplitagain[1]+':'+linesplitagain[3]
                if string not in set1:
                    set1.add(string)
                    f_result_mutate.write(string)
                    f_result_mutate.write('\n')'''
            string=linesplitagain[1]+':'+linesplitagain[3]
            if string not in set1:
                set1.add(string)
                f_result_mutate.write(string)
                f_result_mutate.write('\n')
        lineNum+=1
    f_distance.close()
     
    f_asa=open(file_asa)
    for line in f_asa:
        line=line.strip('\n')
        linesplit=line.split(':',3)
        string=linesplit[0]+':'+linesplit[1]
        if float(linesplit[3])>=0.5 and string not in set1:
            '''if linesplit[2]!='ALA' and linesplitagain[2]!='GLY':
                set1.add(string)
                f_result_mutate.write(string)
                f_result_mutate.write('\n') '''
            set1.add(string)
            f_result_mutate.write(string)
            f_result_mutate.write('\n') 
    f_asa.close()
    f_result_mutate.close()
    return resultfile
            
