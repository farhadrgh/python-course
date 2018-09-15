# sigam(1/x) when x goes to positive infinity
# Farhad Ramezanghorbani	

step=1						# set step to 1		
sigma=0.0					# set sigma of 1/x to 0
error=10**(-6)					# def err (which is subtraction-
						# of two consequent sigma)
pytresult=open("hw21result.txt","w")		# open an empty .txt for writing the result
def div(x):					# define division of 1/x as function
	return 1.0/x
while 1:					# open an infinite loop to calculate-
	sigma+=div(step)			# sigma untill the subtraction of two- 
	if div(step)<=error:			# consequent sigma is equal to defined err
		break
	output=str(sigma)+"	"+str(step)+"\n"# output as two columns (sigma vs #step)
	result.write(output)			# write result in txt file
	step+=1					

print sigma

# as we can see Sigma(1/x) goes to infinity when x goes to infinity but the slope of graph will decrease after 10*5 steps
# I have defined the error in which the infinit loop of while will stop when the division of two consequent sigma is less than 10 to the power of -6

