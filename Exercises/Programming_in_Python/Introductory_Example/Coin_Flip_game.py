#Write a program that prints one realization of the following random device:

#Flip an unbiased coin 10 times
#If 3 consecutive heads occur one or more times within this sequence,
#pay one dollar
#If not, pay nothing

from random import uniform

def coin_game():
	count=0
	result="Pay Nothing"
	for i in range(10):
		U=uniform(0,1)
		if U< 0.5:
			count=count+1
		if U>=0.5:
			count=0
		if count==3:
			result="Pay $1"
	print result





