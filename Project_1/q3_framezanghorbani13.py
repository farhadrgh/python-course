
class Polynomial:
	
	def __init__(self, pol):
		self.pol = pol


	def printpoly(self, expo):
		if self.pol.has_key(expo) == 1:
			polyprint = self.pol[expo]
		else:
			polyprint = 0
		return polyprint

	def calc(self, x):
		p = 0
		for k in self.pol.keys():			
			p += self.pol[k]*(x**k)
		return p

		
sample_dict = {0:2, 1:3, 2:7}
y = Polynomial(sample_dict)
x = -1
expo = 3

print "poly_dictionary(exponent:coefficient): ", y.pol
print "printpoly of %d = %d" % (expo, y.printpoly(expo))
print "value of poly for %d = %d" % (x,y.calc(x))
