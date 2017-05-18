#Python implementation of a simple two layer neural network, which computes an XOR of a given input

import numpy as np
import time 

#input variables 
n_hidden=10
n_in=10

#output variables 
n_out=10

#No of Sample data 
n_sample=300

#Hyperparameters 
learning_rate =0.01
momentum=0.9

#Non-Deterministic seeding 
np.random.seed(0)

def sigmoid(x):
	return 1.0/(1.0+np.exp(-x))

def tanh_prime(x):
	return 1-np.tanh(x)**2

def train(x,t,V,W,bV,bW):

	#forward propogation 
	A=np.dot(x,V)+bV
	Z=np.tanh(A)

	B=np.dot(Z,W)+bW
	Y=sigmoid(B)


	#backword propogation 
	Ew=Y-t
	Ev=tanh_prime(A)*np.dot(W,Ew)


	#predict our loss
	dW=np.outer(Z,Ew)
	dV=np.outer(x,Ev)

	#cross entropy 
	loss=np.mean(t*np.log(Y)+(1-t)*np.log(1-Y))

	return loss, (dV,dW,Ev,Ew)


def predict(x,V,W,bV,bW):
	A=np.dot(x,V)+bV
	B=np.dot(np.tanh(A),W)+bW

	return (sigmoid(B)>0.5).astype(int)

#create layers 
V=np.random.normal(scale=0.1,size=(n_in,n_hidden))
W=np.random.normal(scale=0.1,size=(n_hidden,n_out))

bV=np.zeros(n_hidden)
bW=np.zeros(n_out)

params=[V,W,bV,bW]

#generating data .............
x=np.random.binomial(1,0.5,(n_sample,n_in))
T=x^1

#Training NN .........
for epoch in range(100):
	err=[]
	update=[0]*len(params)

	t0=time.clock()

	for i in range(x.shape[0]):

		loss,grad=train(x[i],T[i],*params)

		#update loss 

		for j in range(len(params)):
			params[j]-=update[j]

		for j in range(len(params)):
			update[j]=learning_rate*grad[j]+momentum*update[j]

		err.append(loss)

	print( "Epoch: %d, Loss: %.8f, Time: %.4fs" % (epoch, np.mean( err ), time.clock()-t0 ))

#Try to predict 

x=np.random.binomial(1,0.5,n_in)
print('XOR Prediction')
print(x)
print(predict(x,*params)) 