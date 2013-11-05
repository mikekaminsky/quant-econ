#Factorial function

def factorial(n):
	answer=0
	if n>0:
		answer=1
		for i in range(n):
			i=i+1
			answer=answer*i
	return answer

factorial(2)