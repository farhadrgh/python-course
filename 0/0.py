#The Game of choosing a number between 0 and 100

import random
Q = (random.randint(0, 100))
print Q
UP = int(100)
Down = int(0)
I = int(0)

while (I==0):
	
	print "your guss should be between" , (Down,UP)
	guss=raw_input ("Enter your guss:\n")
	guss=int(guss)

	if guss==Q:
		I=int(1)
	if guss<Q:
		Down=guss	
	if guss>Q:
		UP=guss


print "Finally you find the computer No. which is: %d" % guss
