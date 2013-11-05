#Part 1: Given two numeric lists or tuples x_vals and y_vals of equal length, 
#compute their inner product using zip()

#Part 2: In one line, count the number of even numbers in 0,...,99

#Hint: x % 2 returns 0 if x is even, 1 otherwise
#Part 3: Given pairs = ((2, 5), (4, 2), (9, 8), (12, 10)),
#count the number of pairs (a, b) such that both a and b are even

x_vals=[1,2,3,4]
y_vals=[1,2,3,4]

#Part 1:
part1=sum([p*q for p,q in zip(x_vals,y_vals)])

#Part 2:
part2=sum(x%2==0 for x in range (0,99))

#Part3:
pairlist=((2, 5), (4, 2), (9, 8), (12, 10))
part3=sum(p%2==0 and q%2==0 for p,q in pairlist)
