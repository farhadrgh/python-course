import re

#filename = str(raw_input("\nenter the input file full name (name.pdb):"))i



def mutate(inputfile, resid):

        file = open(inputfile, "r")
        output = open("output.pdb", "w")

	lines = file.readlines()
	temp = lines
	expression1 = r"^ATOM"
	expression2 = ["N","CA","C","O"]
	for line in temp:
		if  re.search(expression1, line):
			if not re.search(resid, line):
				for exp in expression2:
					if line.split()[2] != exp: 
						temp.remove(line)	

					else:
                                		oldres = line[17:20]
                                		line = line.replace(oldres, resid, 1)
#	for newline in lines:
	print >> output, temp
	#	print >> output, line
	file.close()
	output.close()
	
x = raw_input("enter name of input:\n")
y = raw_input("enter residu name:\n")
resid = str(y)
mutate(x,resid)
