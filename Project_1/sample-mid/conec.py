
import math

class Cone:
	"""ffyfl"""

	def __init__(self):
		"""aaaa"""
		
		self.radius=1.0
		self.height=1.0


	def surfarea(self,radius,height):	
		"""aaa"""

		self.radius=radius
		self.height=height
		print "@@@",self.radius		
		print "@@@@",self.height			
		b=math.sqrt (int(self.radius)**2+int(self.height)**2)		
		a=3.14*int(self.radius)*(int(self.radius)+ b)
		return a
 


	def volume(self,radius,height):
		"""aaaa"""

		self.radius=radius
		self.height=height		
		
		d=int(self.radius)**2
		e=int(self.height)			
		c=0.3333*3.14*(d)*e
		return c

#	def add(self):
#		"""aa"""


