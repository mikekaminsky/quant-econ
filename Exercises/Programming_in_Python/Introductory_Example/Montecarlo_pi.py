from __future__ import division
from random import uniform
from math import sqrt

# Montecarlo estimate of Pi

#Imagine a circle of diameter 1 (r=0.5) embedded in the unit
#square. 

#The area (A) =pi * 0.5^2
#So pi=A/(0.5^2)=A/(1/4)=A*4


def montecarlo_pi(n):
	count=0
	for i in range(n):
		#Select x and y coordinates from a uniform random
		#distribution
		x,y=uniform(0,1), uniform(0,1)
		#Here we are estimating the distance from the center of the unit square located at point (0.5,0.5)
		d=sqrt((x-0.5)**2 + (y-0.5)**2)
		#If the distance is less tahn 0.5 (the radius of the enscribed circle), then the point falls
		#within the circle
		if d<0.5:
			count +=1
	#The area estimate is the share of points in the enscribed circle over the total number of points
	#drawn
	area_estimate=count/n

	print "Using "+str(n)+" iterations, the estimate of pi is "+str(area_estimate*4)

montecarlo_pi(100)
montecarlo_pi(1000)
montecarlo_pi(10000)
montecarlo_pi(100000)
