#! /usr/bin/python

from __future__ import division
import math

class Data:
    ''' Data class '''

    def __init__(self,data):
        self.data = data

    def mode(self):
        ''' Returns mode as a float when data has only one mode
            returns a list of modes when there are multiple modes '''
        
	counts = {}				#it should be list 
	maxcount = 0
        for item in self.data:			#
            counts[item] = 0			#
	for item in self.data:
            counts[item] += 1
            if maxcount < counts[item]:		#I reversed the ">"
                maxcount = counts[item]
                mode = item

	mode = []				# mode list        	
	for item in counts:			#
	    if (counts[item] == maxcount):	#
		mode.append(item)		#
        return mode


    def mean(self):
	''' Returns mean of data set'''

	counter = 0.0
	asum = 0.0
	for i in self.data:
	    asum += i
	    counter += 1
	m = asum/counter
	return m
	

    def var(self):
	'''Returns variance of data set'''
	
	s = 0
	for i in self.data:
		s += (i-self.mean())**2	
	v = s/(len(self.data)-1)
	return v	




#Sample data with mode=1 with frequency 2.
#sample_data=[1,2,3,4,5,6,1]
#Sample data with two modes (1 and 2) with frequency 2.
sample_data=[1,3,2,2,3,4,5,6,1]

x = Data(sample_data)


print 'Data\t\t:', x.data

print 'Mode\t\t: ', x.mode()

print 'Mean\t\t: %.4f' %x.mean()

print 'Var\t\t: %.4f' %x.var()
#print 'Std\t\t: %.4f' %x.std()
