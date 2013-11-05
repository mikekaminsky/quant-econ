#Your next task is to simulate and plot the correlated time series
#x_{t+1}=\alpha x_t+\epsilon_{t+1}
#where x_0=0 and t=0,…,T
#The sequence of shocks {\epsilon_t} is assumed to be iid and standard normal

#In your solution, restrict your import statements to

from pylab import plot, show,legend
from random import normalvariate

#Set T=200 and a=0.9

def corr_time_simulation(periods,alpha):
	x_i=0
	global x_values
	x_values=[]
	for i in range(periods):
		x_values.append(x_i)
		x_i=alpha*x_i+normalvariate(0,1)

corr_time_simulation(200,0)
plot(x_values, label='alpha = '+str('0.0'))
corr_time_simulation(200,0.8)
plot(x_values, label='alpha = '+str('0.8'))
corr_time_simulation(200,0.98)
plot(x_values, label='alpha = '+str('0.98'))
legend()
show()		


