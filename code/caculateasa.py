#!/usr/bin/env python



def caculateasa(file1,file2,file3='new.txt'):
    import sys
    file_1=open(file1) #antigen's value of sum
    lenfile_1=0;
    file_1_load = []
    for line in file_1:
        line=line.strip('\n')
        loadcontains=line.split(':',4)
        file_1_load.append(loadcontains)
        lenfile_1+=1
    file_1.close()
    file_2=open(file2)
    file_2_load = []
    lenfile_2=0
    for line in file_2:
        line=line.strip('\n')
        loadcontains=line.split(':',4)
        if loadcontains[0]== file_1_load[lenfile_2][0] and loadcontains[1] ==file_1_load[lenfile_2][1]:
            file_2_load.append(loadcontains)
            lenfile_2+=1
        elif lenfile_2 > 0:
            print('the number is preductive')
            exit(1)
        if lenfile_2 == lenfile_1:
            break;
    file_2.close()
    f_result=open(file3,'w')
    for i in xrange(0,lenfile_2):
        if float(file_1_load[i][4])==0 and float(file_2_load[i][4])==0:
            resultasa=0
        else:
            resultasa=(float(file_1_load[i][4])-float(file_2_load[i][4]))/float(file_1_load[i][4])
        print(file_1_load[i][0]+':'+file_2_load[i][1]+':asa=%s '% resultasa)
        f_result.write(file_1_load[i][0]+':'+file_1_load[i][1]+':'+file_1_load[i][2]+':%s'% resultasa)
        f_result.write('\n')
    f_result.close()





def main():
    import argparse
    parser=argparse.ArgumentParser() 
    parser.add_argument('-o1', action='store', required=True, dest='file1',
                    help='file1 is needed ,it\'a result of asa ')
    
    parser.add_argument('-o2', action='store', required=True, dest='file2',
                    help='file2 is needed,it\'a result of asa')
    parser.add_argument('-o3', action='store', required=False, dest='file3',
                    help='not need,it\'s default to new.txt')
    input=parser.parse_args()
    caculateasa(input.file1,input.file2,input.file3)
    print('Done,the result have stored in ',input.file3)


if __name__=="__main__":
    print "in main"
    main()
