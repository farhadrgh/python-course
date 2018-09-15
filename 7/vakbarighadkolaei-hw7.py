import random

class Cell:
    """Single Cell in a data structure"""
   
    def __init__( self, value, colindex ):
        """Cell constructor"""
          
        self._value = value
        self._colindex = colindex
        self._nextCell = None
      
    def __str__( self ):
        """Cell data representation"""
   
        return str( self._value )

class Row:
    """Linked Row"""

    def __init__( self, rowindex ):
        """Row constructor"""
        self._rowindex = rowindex
        self._firstCell = None
        self._nextRow = None

    #overloaded print function for the row
    def __str__( self ):
       """Row string representation"""
       if self.EmptyRow(): #chek if the row is empty
            return "empty"
  
       currentCell = self._firstCell
       output = []
       while currentCell is not None:
            output.append( str( currentCell._value ) )
            currentCell = currentCell._nextCell
   
       return " ".join( output )      
           
    def insertAtBack( self, value, colindex):
        """Insert Cell at back of Row"""
   
        newCell = Cell( value,colindex)
                
        if self.EmptyRow():  # Row is empty
            self._firstCell  = newCell
            self._currentCell = self._firstCell 
        else:  # Row is not empty
            self._currentCell._nextCell =  newCell
            self._currentCell = newCell
    
    #build a row with all zeros (we will use it for overloaded print function for sparse class
    def allzerorow (self, colindex):
        """build an all zero row"""
        
        newCell =  Cell (0, colindex)
        self._firtCell = newCell
        for i in range (colindex):
            newCell = Cell(0,i)
            newCell._nextCell = self._firstCell
            self._firstCell = newCell  
    
    #when we find a positive value in a row we insert zero for all the values behind it
    def insertAtFront( self, colindex):
        """Insert node at front of list"""
      
        for i in range (colindex):
            newCell = Cell( 0,colindex )
            newCell._nextCell = self._firstCell
            self._firstCell = newCell            
   
    def EmptyRow (self) :
        """ Return true if row is empty"""
        if self._firstCell is None:
            return True
        else:
            return False
            
class Sparse:
    """Linked Sparse"""

    def __init__( self, nrow, ncol ):
        """Sparse constructor"""
        self._nrow = nrow
        self._ncol = ncol
        self._firstRow = None
 
    def __str__( self ):
       """Row string representation"""
       output = "\n"  #the output value for printing
       downside = -1  #this value helps to organize the rowindexes
       currentRow = self._firstRow

       while currentRow  is not None:
            #the case that some first rows are only included of zeroes
            if downside == -1 and currentRow._rowindex >= 1:
                for i in range (0,currentRow._rowindex):
                    newRow = Row(i)
                    newRow.allzerorow(self._ncol)
                    output += str(newRow) + "\n"

            #the case that some rows between two nonzero rows are only included of zeroes            
            elif downside != -1 and currentRow._rowindex >= (downside+2):
                for i in range (downside+1,currentRow._rowindex):
                    newRow = Row(i)
                    newRow.allzerorow(self._ncol)
                    output += str(newRow) + "\n" 
            
            output += str(currentRow) + "\n"
            downside = currentRow._rowindex
            currentRow = currentRow._nextRow
            
       # the case that some of the last rows are only zeroes
       if downside > -1 and downside !=  self._nrow:
            for i in range (downside+1,self._nrow):
                newRow = Row(i)
                newRow.allzerorow(self._ncol)
                output += str(newRow) + "\n"

       # the case that whole matrix is zero
       elif downside == -1 :
            for i in range (0,self._nrow):
                newRow = Row(i)
                newRow.allzerorow(self._ncol)
                output += str(newRow) + "\n"                                

       return " ".join( output )     
   
    #inserting nonzero rows to sparse
    def insertrow ( self, rowindex):
        """Insert Row at back of Sparse"""        
                        
        if self.EmptySparse():  # Sparse is empty
            self._firstRow  = newRow
            self._currentRow = self._firstRow 
        else:  # Sparse is not empty
            self._currentRow._nextRow =  newRow
            self._currentRow = newRow
    
    def EmptySparse (self) :
        """ Return true if sparse is empty"""

        if self._firstRow is None:
            return True
        else:
            return False   
    
                                            
# generate a random matrix 
# number of rows = nRow
# number of Columns = nCol
# Alpha = sparsity of matrix

def genmat(nRow,nCol,alpha):
    mat = []
    i = 0;
    while i < nRow:
        rows = []
        j = 0
        while j < nCol:
            rn=random.random()
            if (rn < alpha):
                rows.append(random.randrange(1,10))
            else:
                rows.append(0)
            j += 1
        mat.append(rows)
        i += 1

    return mat
    
n = random.randrange(2,20) #number of rows - a random number
m = random.randrange(2,20) #number of columns - a random number
alfa = 0.1 #sparsity of the matrix
matrix = genmat(n,m,alfa) #generate a random matrix with n rows and m columns
print matrix #printing the random generated matrix

sparse = Sparse (n,m) #building the sparse class with number of rows and columns as its input

for i in range (n):
    for j in range (m):
        if matrix [i][j] > 0:
            newRow = Row(i) #if a value is positive we build a row for it
            newRow.insertAtBack (matrix [i][j],j) #entering the value in the row linked list
            newRow.insertAtFront(j) #entering all the zero values behind that
            for h in range (j+1,m): #entering remaining values to the list to make it a complete row
                newRow.insertAtBack (matrix [i][h],h)
            print newRow #check to see the rows (we only built rows with at least one positive element on it)
            sparse.insertrow (i) # adding the row with positive value to the sparse class
            break

print sparse # printing the over loaded print function for sparse class
# it supposed to show the whole matrix, including those without positive elements



        
    

