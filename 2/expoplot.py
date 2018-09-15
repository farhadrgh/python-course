# Taylor expansion of e**x
# for different inputs of n and x

import math
import random
nc=0
error=10**(-100)
result=open("hw22expoplot.txt","w")

#	for nc in range(10000):
		expo=0.0
		n=0.0
#		x=15*random.random()
		#x=float(raw_input("enter x of e**x "))
	
		def div_fact(x):
			return float(x**n/math.factorial(n))

		while 1:
			expo+=div_fact(x)
			if div_fact(x)<=error:
				break
			n+=1
			output=str(n)+"		"+str(expo)+"\n"
			#print n,math.factorial(n),math.exp(x)-expo
		#output=str(x)+"	"+str(expo)+"\n"	
		result.write(output)
		#nc+=1
