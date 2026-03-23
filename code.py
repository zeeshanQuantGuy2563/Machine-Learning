import numpy as np
import math
a=np.array([1,2,3,4,5,6,7,8,9,10])

#Various operations on arrays.
print(a)
print(a.shape) #Tells us about the shape of an array int the form of(rows,colums,depth)
print(a[0])
print(a[1])
print(a[:4])  #Only the index from [0,n-1] is printed.
print(a[2:])  #Only the index from [idx,len(a)] is printed.
a[0]=40       #Item assignment can be done as the array is mutable.
a[1]=50
print(a)
print(a.ndim)                #Tells us about the dimension of an array.
print(len(a.shape)==a.ndim)  #verification
print(a.size)                      # Tells us about the no. of elemants in the array.
print(a.size==math.prod(a.shape))  # verification
print(a.dtype) #Tells us about data type of homogeneous elements.


#Array generation.
print(np.zeros(3)) #Only one dimensional array of zeroes will be created.
print(np.ones(3)) #Only one dimensional array of ones will be created.
print(np.empty(4)) #Initial content is random and depends on the state of the memory. 
print(np.arange(1,9,1)) #create an array np.arange(first element, last element+1, stepsize)
print(np.linspace(1,6,4)) #A function the creates an array evenly spaced between two digits with no. of desired values. np.linspace(first number, last number, desired number of elements you want)
print(np.zeros(3,dtype=np.int64)) #(dtype=np.int64) write this function as defined in example to declare the data type you want your data in for any array creation menthod. 

#sorting but very basic
arr=np.array([2,3,8,5,7,2,9,10,35,67,100,50,37])
print(np.sort(arr))

#concatenation of arrays
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
print(np.concatenate((arr1,arr2)))

x=np.array([[1,2,3,4],[3,4,5,6]])
y=np.array([[5,6,7,8]])

print(np.concatenate((x,y),axis=0))


