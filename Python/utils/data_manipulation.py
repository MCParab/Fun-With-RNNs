from __future__ import division 
import numpy as np
import math
import sys 


def shuffle_data(X,y,seed=None):
	#concatenate x and y and do random shuffle 
	X_y=np.concatenate((X,y.reshape((1,len(y))).T),axis=1)
	if seed:
		np.random.seed(seed)
	np.random.shuffle(X_y)
	X=X_y[:,:-1] #every column except the last
	y=X_y[:,-1]  #last column 

    return X,y


 #Divide dataset based on if sample value on feature index in larger than 
 #the given threshold 

 def divide_on_feature(X,feature_i,threshold):
 	split_func=None
 	if isinstance(threshold, int) or isinstance(threshold, float):
 		split_func=lambda sample:sample[feature_i]>=threshold
 	else:
        split_func=lambda sample: sample[feature_i]==threshold

    X_1=np.array([sample for sample in X if split_func(sample)])
    X_2=np.array([sample for smple in X if not split_func(sample)])

    return np.array([X1,X2])