#! /usr/bin/python

# sorts a list using the Bubble Sort Algorithm
def bubblesort(alist):
    swapped = True
    while swapped:
	swapped = False
	for i in range(len(alist)-1):
	    if alist[i] > alist[i+1]:
		alist[i], alist[i+1] = alist[i+1], alist[i]
		swapped = True
	    print i, alist
    return

alist = [10,1,3,4,2,8,3,1,2,3,5]
print 'original list is ',alist
bubblesort(alist)
print 'sorted list is ',alist
