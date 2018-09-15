import copy
class Polynomial:
    
	def __init__(self, dictpoly={}):
		"""initializing dictionary of polynomial"""
		self.dictpoly = dictpoly
    
	def printpoly(self, expo):
		"""print coefficient of each needed exponent"""
		if self.dictpoly.has_key(expo) == 1:
			polyprint = self.dictpoly[expo]
		else:
			polyprint = 0
		return polyprint

	def __str__(self):
		"""defining method str for representin poly as str"""
		self.str = ""   
        	for key,value in self.dictpoly.items():
            		if value==0:
                		self.str += ""
            		elif value>0:
                		sign = "+"
                		self.str += sign
                		self.str += str(value) +"X**"+ str(key)
            		elif value<0:
                		self.str += str(value) +"X**"+ str(key)
		return self.str
        
    	def __len__(self):
		"""modifying the length function""" 		#it will give us the highest value 
		return max(self.dictpoly.keys())		#of exponent in a polynomial
    	
	def __add__(self,other):
		"""modifying add operator"""			#it will give us the result of 
	        copydictpoly = copy.deepcopy(self.dictpoly)	#adding two polynomials
	        for key in other.dictpoly.keys():
	            	if key in self.dictpoly:
                		copydictpoly[key] += other.dictpoly[key]
            		else:
                		copydictpoly[key] = other.dictpoly[key]
        	return Polynomial(copydictpoly)
    
    	def __sub__(self,other):
		"""modifying subtraction operator"""		#it will give us the result of
        	copydictpoly = copy.deepcopy(self.dictpoly)	#subtraction of two polynomials
        	for key in other.dictpoly.keys():
        	    	if key in self.dictpoly:
                		copydictpoly[key] -= other.dictpoly[key]
            		else:
                		copydictpoly[key] = -other.dictpoly[key]
        	return Polynomial(copydictpoly)
            
            
### Importing polynomials by user ################  

dict1 = {}
decision1 = str('y')

print "enter polynomial1 terms"
while(decision1 == 'y'):
    	expo1 = int(raw_input("enter exponent value \n"))
    	coef1 = int(raw_input("enter coeff value \n"))
    	dict1[expo1]=coef1
    	decision1 = raw_input("y to enter another term, n to polynomial2\n")

dict2 = {}
decision2 = str('y')

print "enter polynomial2 terms"
while(decision2 == 'y'):
    	expo2 = int(raw_input("enter exponent value \n"))
    	coef2 = int(raw_input("enter coeff value \n"))
    	dict2[expo2]=coef2
    	decision2 = raw_input("y to enter another term, press n to exit\n")

pol1 = Polynomial(dict1)
pol2 = Polynomial(dict2)

##################################################

print "polynomial1 =\t", pol1
print "highest exponent of polynomial: ", len(pol1)

print "polynoimal2 =\t", pol2
print "highest exponent of polynomial: ", len(pol2)

print "polynomial1 + polynomial2 =\t", pol1+pol2
print "polynomial1 - polynomial2 =\t", pol1-pol2

##################################################
