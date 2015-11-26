import sys
import os
import argparse
import __main__
__main__.pymol_argv=['pymol','-rqkc'] #pymol quiet and no GUI
try :
    import pymol
    del pymol
except ImportError :
    print "pymol has not been installed on this system.Please install it from the following link:"
    print "http://www.pymol.org/"
    sys.exit(1)
    pass
import pymol
from pymol import cmd, stored, math

 
def pairwise_dist(pdbfile,sel1, sel2, max_dist, output="P", sidechain="N", show="N",outfile="./"):
	"""
	usage: pairwise_dist sel1, sel2, max_dist, [output=S/P/N, [sidechain=N/Y, [show=Y/N]]]
	sel1 and sel2 can be any to pre-existing or newly defined selections
	max_dist: maximum distance in Angstrom between atoms in the two selections
	--optional settings:
	output: accepts Screen/Print/None (default N)
	sidechain: limits (Y) results to sidechain atoms (default N)
	show: shows (Y) individual distances in pymol menu (default=N)
	"""
	print ""
	cmd.delete ("dist*")
	extra=""
	if sidechain=="Y": extra=" and not name c+o+n"
 
	#builds models
	m1=cmd.get_model(sel2+" around "+str(max_dist)+" and "+sel1+extra)
	m1o=cmd.get_object_list(sel1)
	m2=cmd.get_model(sel1+" around "+str(max_dist)+" and "+sel2+extra)
	m2o=cmd.get_object_list(sel2)
 
	#defines selections
	cmd.select("__tsel1a", sel1+" around "+str(max_dist)+" and "+sel2+extra)
	cmd.select("__tsel1", "__tsel1a and "+sel2+extra)
	cmd.select("__tsel2a", sel2+" around "+str(max_dist)+" and "+sel1+extra)
	cmd.select("__tsel2", "__tsel2a and "+sel1+extra)
	cmd.select("IntAtoms_"+str(max_dist), "__tsel1 or __tsel2")
	cmd.select("IntRes_"+str(max_dist), "byres IntAtoms_"+str(max_dist))
 
	#controlers-1
	if len(m1o)==0: 
		print "warning, '"+sel1+extra+"' does not contain any atoms."
		return
	if len(m2o)==0: 
		print "warning, '"+sel2+extra+"' does not contain any atoms."
		return
 
	#measures distances
	s=""
	counter=0
	for c1 in range(len(m1.atom)):
		for c2 in range(len(m2.atom)):
			distance=math.sqrt(sum(map(lambda f: (f[0]-f[1])**2, zip(m1.atom[c1].coord,m2.atom[c2].coord))))
			if distance<float(max_dist):
				s+="%s/%s/%s/%s/%s to %s/%s/%s/%s/%s: %.3f\n" % (m1o[0],m1.atom[c1].chain,m1.atom[c1].resn,m1.atom[c1].resi,m1.atom[c1].name,m2o[0],m2.atom[c2].chain,m2.atom[c2].resn,m2.atom[c2].resi,m2.atom[c2].name, distance)
				counter+=1
				if show=="Y": cmd.distance (m1o[0]+" and "+m1.atom[c1].chain+"/"+m1.atom[c1].resi+"/"+m1.atom[c1].name, m2o[0]+" and "+m2.atom[c2].chain+"/"+m2.atom[c2].resi+"/"+m2.atom[c2].name)
 
	#controler-2
	if counter==0: 
		print "warning, no distances were measured! Check your selections/max_dist value"
		return
 
	#outputs
	if output=="S": print s
	if output=="P":
                filename=os.getcwd()+'/interface_analyzer/'+pdbfile+'_distance'+str(max_dist)
		f=open(filename,'w')
		f.write("Number of distances calculated: %s\n" % (counter))
		f.write(s)
		f.close()
		print "Results saved in _%s" % filename 
	print "Number of distances calculated: %s" % (counter)
	cmd.hide("lines", "IntRes_*")
	if show=="Y": cmd.show("lines","IntRes_"+max_dist)
	cmd.deselect()
 
cmd.extend("pairwise_dist", pairwise_dist)
def main():
    parser=argparse.ArgumentParser()
    
    parser.add_argument('-f', action='store', required=True, dest='pdbfile',
                    help='PDB file of protein-antibody complex')
  
    parser.add_argument('-d', action='store', required=True, dest='distance',
                    help='distance is more than 0')
    inputs=parser.parse_args()
    from os import path,access,R_OK
    
    pdbfile=inputs.pdbfile
    distance=inputs.distance
    if path.exists(pdbfile) and path.isfile(pdbfile) and access(pdbfile,R_OK):
        pass
    else:
        print "Your PDB file does not exist. Please check the path of your PDB file."
	sys.exit(1)
    print "Extracting out the residues with cut off with 4"
    pymol.finish_launching()
    pymol.cmd.load(pdbfile)
    pymol.cmd.remove('hydrogens')
    pymol.cmd.remove('solvent')
    pairwise_dist(pdbfile,'not chain L+H','chain L+H',float(distance),'P')
    pymol.cmd.delete(all)
    pymol.cmd.quit()

if __name__=="__main__":
    print "in main"
    main()
