from math import *
from numpy import *
import pylab as pl
from numpy.linalg import *

####################################### coefficient matrix of forces:
A=matrix('0 1 0 0 0 -1 0 0 0 0 0 0 0 ; 0 0 1 0 0 0 0 0 0 0 0 0 0 ; 0.7071 0 0 -1 -0.7071 0 0 0 0 0 0 0 0 ; 0.7071 0 1 0 0.7071 0 0 0 0 0 0 0 0 ; 0 0 0 1 0 0 0 -1 0 0 0 0 0 ; 0 0 0 0 0 0 1 0 0 0 0 0 0 ; 0 0 0 0 0.7071 1 0 0 -0.7071 -1 0 0 0 ; 0 0 0 0 0.7071 0 1 0 0.7071 0 0 0 0 ; 0 0 0 0 0 0 0 0 0 1 0 0 -1 ; 0 0 0 0 0 0 0 0 0 0 1 0 0 ; 0 0 0 0 0 0 0 1 0.7071 0 0 -0.7071 0 ; 0 0 0 0 0 0 0 0 0.7071 0 1 0.7071 0 ; 0 0 0 0 0 0 0 0 0 0 0 0.7071 1')
####################################### constant matrix in AX = B:
B=matrix('0 ; 10 ; 0 ; 0 ; 0 ; 0 ; 0 ; 15 ; 0 ; 20 ; 0 ; 0 ; 0')
####################################### soloution of AX = B:
x = solve(A,B)
print "fi values for i in [1,13]\n", x
print A
print B
#####################################################################
n = linspace(pi/100,pi/2.1,1000) #list of 1000 number in [pi/100,pi/2.1]

List = []
for t in n:						 #change alpha in coefficient matrix
								 #considering the angle of 1-3-2
	A[2,0] = sin(t)
	A[2,4] = -sin(t)
	
	A[3,0] = cos(t)
	A[3,4] = cos(t)
	
	A[6,4] = sin(t)
	A[6,8] = -sin(t)
	
	A[7,4] = cos(t)
	A[7,8] = cos(t)
	
	A[10,8] = sin(t)
	A[10,11] = -sin(t)
	
	A[11,8] = cos(t)
	A[11,11] = cos(t)
	
	A[12,11] = sin(t)
	
	y = solve(A,B)
	List.append(abs(y).max())


pl.plot(n,List)
pl.show()

	

