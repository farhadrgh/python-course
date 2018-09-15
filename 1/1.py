# Monte Carlo Integration
# Calculating pi number
# Farhad Ramezanghorbani



import random					# Call random function
n=1
#result=open("result.txt","w")			# Open a txt file for writing the result
while (n<=100):
	s=100000*n				# Number of steps for each entry of n
	t=0.0						
	c=0.0
	while (t<=s):			
		x=random.random()		# Random number for x coordinate of point
		y=random.random()		# Random number for y coordinate of point
		r=(float(x**2)+float(y**2))		
		if (r<=1):			# Check if that point is in the sircle
			c+=1				
		t+=1				# Anyway it will add 1 to total number of points
	p=4*(c/t)				# Calculate pi number
#	output=str(p)+"		"+str(s)+"\n"	# Change the typ of result to string
#	result.write(output)			# Write result in the defined file
	print p					# Show result on the screen
	n+=1						







