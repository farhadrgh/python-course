import sys, cPickle
file = open( "users.dat", "w" )

print "Enter the user name, name and date of birth."
print "Enter end-of-file to end input."
inputList = []
while 1:
	try:
		accountLine = raw_input( "? " )
	except EOFError:
		break
	else:
		inputList.append( accountLine.split() )

cPickle.dump( inputList, file )
file.close()

