##Python implementation of tuple data structure

##Declaring tuples
tup1=('physics','chemistry',1997,2000)
tup2=(1,2,3,4,5)
tup3="a","b","c","d"

##single value insertion in tuple
tup4=(50,)

##Accessing values from a tuple
print ("tup1[0] = ", tup1[0])  ##tup1[0] =  physics
print ("tup2[1:4]",tup2[1:4])  ##tup2[1:4] (2, 3, 4)

##Updating tuples -- Tuples are immutable which means you cannot update or 
#change the values of tuple elements. You are able to take portions of existing tuples to 
#create new tuples as the following example demonstrates 
tup5=("xyz","abc")
tup6=(43,44)
tup7=tup5+tup6
print (tup7 )##tup7 :  ('xyz', 'abc', 43, 44)

##Deleting tuples -- deleting elements of tuples is not possible, we can 
#delete the whole tuple 
del tup7 

##Basic tuple operations 
print (len((1,2,3))) ##3
print ((1,2,3)+(4,5,6)) ##(1, 2, 3, 4, 5, 6)
print (("Hi")*4) ##HiHiHiHi
print (3 in (1,2,3)) ##True

for x in (1,2,3):
   print (x)
"""
1
2
3
"""
##Tuple built-in function 

#len() -- returns length of a tuple 
tup10=(1,2,3,4,5,6)
print("Length of tup10 : ",len(tup10)) ##Length of tup10 :  6

#max() --returns maximum no of tuple
print("Max of tup10 : ",max(tup10)) ##Max of tup10 :  6

#min() --returns maximum no of tuple
print("Min of tup10 : ",min(tup10)) ##Min of tup10 :  1

#tuple() --converts a sequence to tuple 
list=[1,2,3,4,5,6,7,8,9,10]
conTup=tuple(list)
print("Tuple elements : ",conTup) ##Tuple elements :  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)