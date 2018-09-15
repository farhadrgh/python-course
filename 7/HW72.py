class Node:
	def __init__ (self,data):
		self.data=data
		self._nextNode=None
	def __str__(self):
		return str (self.data)
###########################################################################

class Cell:
	def __init__(self,data):
		n=len(data)

		k=0
		while 1:
			if data[k] != 0:
	 			self._firstNode=Node(k+1)
				currentNode=self._firstNode
				break			
			else:
				k=k+1				

		for j in range (k+1,n):
			if data[j] != 0:
				newNode=Node(j+1)
				currentNode._nextNode=newNode
				currentNode=newNode
				
		self._lastNode=currentNode

	def __str__(self):
		if self.isEmpty():
			return "empty"
		currentNode=self._firstNode
		output=[]
		while currentNode is not None:
			output.append(str( currentNode.data))
			currentNode=currentNode._nextNode
		return "".join(output)

	def isEmpty(self):
		return self._firstNode is None

		return	tempNode


###################################################################################

class Row:
	def __init__(self,data):
		n=len(data)

		for i in range (n):
				for j in range (n):
					if data[i][j] != 0:
						self._firstNode=Node(i+1)
					        currentNode=self._firstNode
				                temp=i
						break
				break
								
		for i in range (temp+1, n):
				for j in range (n):
					if data[i][j] != 0:
						newNode=Node(i+1)
						currentNode._nextNode=newNode
						currentNode=newNode
						break
		self._lastNode=currentNode



	def __str__(self):
		if self.isEmpty():
			return "empty"
		currentNode=self._firstNode
		output=[]
		while currentNode is not None:
			output.append(str( currentNode.data))
			currentNode=currentNode._nextNode
		return "".join(output)

	def isEmpty(self):
		return self._firstNode is None

		return	tempNode

###########################################################################

class Sparse:
	def __init__(self,data):
		n=len(data)

		k=0
		while 1:
			if data[k] != 0:
	 			self._firstNode=Node(data[k])
				currentNode=self._firstNode
				break			
			else:
				k=k+1				
		j=1
		for i in range (k+1,n):
			if data[i] != 0:
				newNode=Node(data[i])
				currentNode._nextNode=newNode
				currentNode=newNode
				
		self._lastNode=currentNode

	def __str__(self):
		if self.isEmpty():
			return "empty"
		currentNode=self._firstNode
		output=[]
		while currentNode is not None:
			output.append(str( currentNode.data))
			currentNode=currentNode._nextNode
		return "".join(output)

	def isEmpty(self):
		return self._firstNode is None

		return	tempNode



		
#data=(3,0,2)
#ListObject=Cell(data)
#print ListObject

matrix=[[1,0,0,0],[0,2,0,0],[0,0,0,0],[0,3,4,0]]
matrixObject=Row(matrix)
print matrixObject


n=len(matrix)

CellObject=Cell(matrix[1])
print CellObject

RowObject=Row(matrix)
print RowObject

sparseObject=Sparse(matrix[1])
print sparseObject




