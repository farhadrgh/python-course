# Fig. 22.3: List.py
# Classes List and Node definition

class Node:
    "Single node in a data structure"
	
    def __init__( self, data ):
	"Node constructor"
	    
	self.data = data
	self.nextNode = None
	
    def getData( self ):
	"Get node data"

	return self.data

    def setData( self, data ):
	"Set node data"

	self.data = data

    def getNextNode( self ):
	"Get reference to next node"

	return self.nextNode

    def setNextNode( self, newNode ):
	"Set reference to next node"

	self.nextNode = newNode

class List:
    "Linked list"
	
    def __init__( self ):
	"List constructor"

	self.firstNode = None
    	self.lastNode = None

    def __str__( self ):
	"Override print statement"

	if self.isEmpty():
	    return "The list is empty"

	currentNode = self.firstNode
	string = "The list is: "

	while currentNode is not None:
	    string += str( currentNode.getData() ) + " "
	    currentNode = currentNode.getNextNode()
	return string

    def insertAtFront( self, value ):
	"Insert node at front of list"

	newNode = Node( value )
	if self.isEmpty():
	    self.firstNode = self.lastNode = newNode
	else:
	    newNode.setNextNode( self.firstNode )
	    self.firstNode = newNode

    def insertAtBack( self, value ):
	"Insert node at back of list"

	newNode = Node( value )
	if self.isEmpty():
	    self.firstNode = self.lastNode = newNode
	else:
	    self.lastNode.setNextNode( newNode )
	    self.lastNode = newNode

    def removeFromFront( self ):
	"Delete node from front of list"

	if self.isEmpty():
	    raise IndexError, "remove from empty list"
	firstNodeValue = self.firstNode.getData()
        if self.firstNode is self.lastNode:
	    self.firstNode = self.lastNode = None
        else:
	    self.firstNode = self.firstNode.getNextNode()
	return firstNodeValue


    def removeFromBack( self ):
	"Delete node from back of list"

	if self.isEmpty():
	    raise IndexError, "remove from empty list"
	lastNodeValue = self.lastNode.getData()
	if self.firstNode is self.lastNode:
	    self.firstNode = self.lastNode = None
	else:
	    currentNode = self.firstNode
	    while currentNode.getNextNode() is not self.lastNode:
		currentNode = currentNode.getNextNode()
	    currentNode.setNextNode( None )
	    self.lastNode = currentNode
	return lastNodeValue

    def isEmpty( self ):
	"Is the list empty?"

	return self.firstNode is None

# Driver to test class List

"""import sys
from List import List"""
 
def instructions():
    "Print instructions for the user"

    print "Enter one of the following:\n", \
 	  " 1 to insert at beginning of list\n", \
 	  " 2 to insert at end of list\n", \
	  " 3 to delete from beginning of list\n", \
	  " 4 to delete from end of list\n", \
	  " 5 to end list processing\n"
 
listObject = List()

instructions()
choice = raw_input("? ")
 
while choice != "5":

    if choice == "1":
 	listObject.insertAtFront( raw_input( "Enter value: " ) )
 	print listObject
    
    elif choice == "2":
 	listObject.insertAtBack( raw_input( "Enter value: " ) )
 	print listObject
 
    elif choice == "3":
 	try:
 	    value = listObject.removeFromFront()
 	except IndexError, message:
 	    print "Failed to remove:", message
    	else:
 	    print value, "removed from list"
 	    print listObject
 
    elif choice == "4":
 	try:
 	    value = listObject.removeFromBack()
	except IndexError, message:
	    print "Failed to remove:", message
 	else:
 	    print value, "removed from list"
 	    print listObject
    else:
 	print "Invalid choice:", choice

    choice = raw_input("\n? ")

print "End list test\n"



