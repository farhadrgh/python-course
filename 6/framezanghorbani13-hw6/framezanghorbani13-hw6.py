################################### farhad ramezanghorbani

while 1:
	try:
		n1 = float(raw_input("enter numerator: "))
		break
	except ValueError:
		print "Error: you should enter float number"

while 1:
	try:
		n2 = float(raw_input("enter denominator: "))
		result = n1/n2
		print "number1 / number2 = ", result		
		break
	except (ValueError, ZeroDivisionError) as e:
		print "Error: ", e
	
	
