# Taylor expansion of e**x in 0 neighburhood
# for different inputs of x

import math					# call the math functions
n=0.0						# set counter of infinite loop
expo=0.0					# set initial # of expo of x to 0
error=10**(-100)				# set error for breaking the infinit loop
x=float(raw_input("enter x of e**x "))		# ask x from user

result=open("hw22result.txt","w")		# open an empty txt for writing the results
	
def div_fact(x):				# define div_fact function which is-
	return float(x**n/math.factorial(n))	# each term of Taylor expansion

while 1:					# open an infinit loop
	expo+=div_fact(x)			# add each term to expo of x till-
	if div_fact(x)<=error:			# the difference between two consequence term-
		break				# is less than error
	n+=1					# go to next term of Taylor expansion	
	output=str(n)+"		"+str(expo)+"\n"# add number of terms vs expo in two column
	result.write(output)			# write the outputs to txt file

# as we can see in the first plot the out put of Taylor expansion will goes to near real number of e**1 after 6 or 7 terms of the expansion
# for x=1 but when we enter 10 for x, what we can see is Taylor expansion needs more terms (about 17-18) to be near the e**10
# so when we write Taylor in 0 neighburhood, for getting the best output our x should be near zero, as you 
# can see in thirs graph, when we enter 0.1 we will be near e**(0.1) after 3 or 4 term.
