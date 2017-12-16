import numpy as np
import matplotlib.pyplot as plt

Ltr=[]
Xtr=[]
Xts=[]
Ytr=[]
Yts=[]
Lts=[]

for i in range(0,1000) :
	x=10*np.random.random()
	y=10*np.random.random()
	Xtr.append(x)
	Ytr.append(y)

	if x<y :
		Ltr.append(1)
		plt.plot(x,y,'bs')
	else :
		Ltr.append(0)
		plt.plot(x,y,'g^') # color='red'


a = 0
b = 0
c = 0
for j in range(0,10):
	for i in range(0,1000) :
		x=Xtr[i]
		y=Ytr[i]
		h=a*x + b*y + c
		l=1 /(1 + np.exp(-h))
		ld=Ltr[i]

		a_grad = (ld - l)*(-x)/(1 + np.exp(-h))*(1 + np.exp(-h))
		b_grad = (ld - l)*(-y)/(1 + np.exp(-h))*(1 + np.exp(-h))
		c_grad = (ld - l)*(-1)/(1 + np.exp(-h))*(1 + np.exp(-h))
	
		a = a - (0.0001)*a_grad
		b = b - (0.0001)*b_grad
		c = c - (0.0001)*c_grad

	

for i in range(0,100) :
	x=10*np.random.random()
	y=(-1)*(c + a*x)/b
	plt.plot(x,y,'ro')


print(a,b,c)

plt.show()


for i in range(0,1000) :
	x_test=10*np.random.random()
	y_test=10*np.random.random()
	Xts.append(x_test)
	Yts.append(y_test)

	if x_test<y_test :
		Lts.append(1)
	else :
		Lts.append(0)


Xts=np.array(Xts)


