
import math
for a in range(1,21):
	for b in range(1,21):
		c = math.sqrt(a**2+b**2)
		if c<=20:
			if c == math.floor(c):
				print "Side1 = %d\tSide2 = %d\tHypotenuse = %d" %(a, b, c)
