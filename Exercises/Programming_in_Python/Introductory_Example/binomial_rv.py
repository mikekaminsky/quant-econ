#Write a function that generates a draw of Y from a binomial
#random distrbution


#Y~Bin(n,p) represents the number of succesful n binary trials, where
#each trial succeeds with probability p

#Hint: if U is uniform on (0,1) and p \in (0,1) then the expression 
#U<p evaluates to True with probability p


from random import uniform

def binomial_rv(n,p):
	count=0
	for i in range(n):
		U=uniform(0,1)
		if U< p:
			count=count+1
	print count


