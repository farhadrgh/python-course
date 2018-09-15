#! /usr/bin/python

import random
import time



def genmat(nRow,nCol,alpha):
    mat = []
    i = 0;
    while i < nRow:
	rows = []
	j = 0
	while j < nCol:
            rn=random.random()
            if (rn < alpha):
                rows.append(1)
            else:
                rows.append(0)
	    j += 1
	mat.append(rows)
	i += 1

    return mat

def printmat(mat):
    n=len(mat)
    m=len(mat[0])
    outstr=""
    for i in range(n):
        for j in range(m):
            outstr += str(mat[i][j])
        outstr += "\n"
    return outstr
    

def mat2sparse(mat):
    sparse = {}
    nRow = len(mat)
    nCol = len(mat[0])
    sparse[-1] = (nRow,nCol)

    i = 0

    while i<nRow:
	j = 0
	while j<nCol:
	    if mat[i][j]:
		sparse[(i+1,j+1)] = mat[i][j]
	    j += 1
	i += 1

    return sparse

def sparse2mat(sparse):
    res = []
    nRow = sparse[-1][0]
    nCol = sparse[-1][1]

    i = 0
    while i<nRow:
	rows = []
	j = 0
	while j<nCol:
	    rows.append(sparse.get((i+1,j+1),0))
	    j += 1
	res.append(rows)
	i += 1
    return res


def matmult(mat1,mat2):
    res = []
    if not len(mat1[0]) == len(mat2):
	print "Error! Matrix dimensions must agree"
	exit(1)
    i = 0
    while i<len(mat1):
	rows = []
	j = 0
	while j<len(mat2[1]):
	    total = 0
	    k = 0
	    while k<len(mat2):
		total += mat1[i][k] * mat2[k][j]
		k += 1
	    rows.append(total)
	    j += 1
	res.append(rows)
	i += 1

    return res

def sparsemult(sp1,sp2):
    res = {}
    if sp1[-1][1] != sp2[-1][0]:
	print "Error! Matrix dimensions must agree"
	exit(1)

    res[-1] = (sp1[-1][0],sp2[-1][1])

    for ind in sp1.keys():
	if not ind == -1:
	    for ind2 in sp2.keys():
		if not ind2 == -1:
		    if ind[1] == ind2[0]:
			i = ind[0];j = ind2[1]
			res[(i,j)] = res.get((i,j),0) + sp1[ind] * sp2[ind2]

    return res


#sp1={(1,1):6,-1:(3,3)}
#sp2={(1,1):3,-1:(3,2)}

n=m=k=300
alpha=0.01

mat1 = genmat(n,m,alpha)
sp1 = mat2sparse(mat1)
mat2 = genmat(m,k,alpha)
sp2 = mat2sparse(mat2)
print "mat1\n",printmat(mat1)
#print sp1
#exit ()
print "mat2\n",printmat(mat2)

start = time.time()
mult = matmult(mat1,mat2)
end = time.time()
#print printmat(mult)
print "time for real matrix multiplication", end-start


start = time.time()
spmult = sparsemult(sp1,sp2)
end = time.time()
#print printmat(sparse2mat(spmult))
print "time for sparse matrix multiplication",end-start



