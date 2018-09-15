import math
import random
#result=open("realplot.txt","w")
def x(y,lan):
	return float(-math.log1p(-y)/lan)

lan=float(raw_input("Enter the value of Landa:\n"))
n=float(raw_input("Number of steps:\n"))
s1=0.0
s2=0.0
s3=0.0
s4=0.0
s5=0.0
s6=0.0
s7=0.0
s8=0.0
s9=0.0
s10=0.0
count=0
while (count <= n):
	y=random.random()
	r=x(y,lan)

	if r<1/lan:
		s1+=1
	elif r<2/lan:
		s2+=1
	elif r<3/lan:
		s3+=1	
	elif r<4/lan:
		s4+=1
	elif r<5/lan:
		s5+=1
	elif r<6/lan:
		s6+=1
	elif r<7/lan:
		s7+=1
	elif r<8/lan:
		s8+=1
	elif r<9/lan:
		s9+=1
	else:
		s10+=1
	#p=float(lan*math.exp(-lan*count))
	#output=str(p)+"\n"
	#result.write(output)
	count+=1
print s1/n
print s2/n
print s3/n
print s4/n
print s5/n
print s6/n
print s7/n
print s8/n
print s9/n
print s10/n

