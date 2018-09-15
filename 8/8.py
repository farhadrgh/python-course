import sys, re
from math import sqrt

# open pdb file

file = open("1UBQ.pdb", "r")
output = open("output.txt", "w")

lines = file.readlines()
print "\npdb file contains %d lines: " % len(lines)

matrixOfData = []
for line in lines:
	matrixOfData.append(line.split())

#############################################################################
print >> output, "lines starting with ATOM at the begining".center(70, "#"),"\n"
ATOM = []
expression1 = r"^ATOM"
for line in lines:
	if re.search(expression1, line):
		print >> output, line
		ATOM.append(line)
print "%d\t lines starting with ATOM" % len(ATOM) 
#############################################################################
print >> output, "lines starting containing LEU in 4th column".center(70,"#"),"\n"
expression2 = r"LEU"
i = 0
for atomline in ATOM:
	if re.search(expression2, atomline):
#	if atomline[17:20] == expression2:
		print >> output, atomline
		i+=1
print "%d\t lines starting with ATOM containing LEU" % i
#############################################################################
print >> output, "lines starting with ATOM\
containing CA in 3rd column".center(70,"#"),"\n"
CA = []
expression3 = r"CA"
i = 0
for atomline in ATOM:
	if re.search(expression3, atomline):
#	if atomline[13:15] == expression3:
		print >> output, atomline
		CA.append(atomline.split())
		i+=1
print "%d\t lines starting with ATOM containing CA" % i
#############################################################################
print >> output, "distance between each pair of CA".center(70,"#"),"\n"

for i in range(len(CA)):

	xi = float(CA[i][6])
	yi = float(CA[i][7])
	zi = float(CA[i][8])
	for j in range(i+1,len(CA)):
		xx = xi - float(CA[j][6])
		yy = yi - float(CA[j][7])
		zz = zi - float(CA[j][8])
		rij = float(sqrt(xx**2+yy**2+zz**2))
	 	print >> output, "distance between %2.dth CA and %2.dth CA\t\
%f".ljust(35) % (i+1,j+1,rij)
#############################################################################
print >> output, "Amino acide sequences".center(70,"#"),"\n"

c = 0
expression4 = r"^SEQRES"
for line in lines:
	if re.search(expression4, line):
		temp = line.split()
		c+=1
		print >> output, "%dth sequence: " % c,
		for i in range(4,len(temp)):
			print >> output, temp[i] ,
		print >> output
#############################################################################
c = 0
for line in lines:
	if re.search(r"^REMARK", line):
		c += line.count("REFERENCE")
print "number of references: %d\n" % c
#############################################################################
print >> output, "Refrences".center(70,"#"),"\n"

ref = []
def Saveref(x):
	ref.append(x)
	print >> output, x

keys = [r"^TITL\s+",r"^AUTH\s+",r"^REF\s+",r"^REFN\s+"]

for line in lines:
	if re.search(r"^REMARK", line):
		if re.search(r"^REFERENCE",line[11:]):
			Saveref(line[11:])
		else:
			for key in keys:
				if re.search(key,line[12:]):
					Saveref(line[12:])
					 

print >> output,"\n","Nature formated references".center(70,"#"),"\n"

title = []
j = 0
for i in range(len(ref)):
	if re.search(r"^AUTH", ref[i]):
		if ref[i][5] == r"\s":
			title.append(ref[i][7:].rstrip())
		else:
			title.insert(j-1,(ref[i-1][7:] + ref[i][7:].strip()))
		j+=1		
print title


		

#		if line.endswith("REFERENCE\s\d\s+"):
#			prine line 
#			continue
#		if line.endswith(r"ISSN\s\d{4}-\d{4}\s+"):
#			print line
#print re.match(r"ISSN\s\d{4}-\d{4}","ISSN 0022-2836")		
#############################################################################
#### reference manipulation:



output.close()
file.close()

