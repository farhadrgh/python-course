import pylab as pl
import numpy as np


x = np.linspace(0.995,1.005,101)
y1 =(x**6-6*x**5+15*x**4-20*x**3+15*x**2-6*x+1)
y2 =((x-1)**6)

#def f(x):
#	return 

pl.plot(x,y1)
pl.plot(x,y2)
pl.legend()
pl.xlim(0.995,1.005)
#pl.ylim(f(0.))
pl.show()
