import sys, cPickle
# open file
try:
	file = open( "users.dat", "r" )
except IOError:
	print >> sys.stderr, "File could not be opened"
	sys.exit( 1 )
records = cPickle.load( file )
 # retrieve list of lines in file
file.close()
print "Username".ljust( 15 ),
print "Name".ljust( 10 ),
print "Date of birth".rjust( 20 )
for record in records:
 # format each line
	print record[ 0 ].ljust( 15 ),
	print record[ 1 ].ljust( 10 ),
	print record[ 2 ].rjust( 20 )

