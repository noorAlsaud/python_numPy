import numpy as np 
x = np.array([1, 2, 3, 4, 5])
print("first element is = ", x[0])
#specify elements from the end by negative indicies 
print("last element is = ", x[-1]) 
print("some element is = ", x[-4]) 
# modify elements : 
x[3] = 20 
print(x)
# 3x3 array containg int from 1 to 9: 
X = np.arange(1, 10).reshape(3,3)
print(X)
print("element 0,0 = ", X[0,0])
print("element 0,1 = ", X[0,1])
print("element 0,2 = ", X[0,2])
X[0, 0] = 20
print(X)
# delete elements: TAKES (3 args) --> Array + List of indices + axis to delete from 

# rank 1 array axis keyword is not required 
R = np.array([1, 2, 3, 4, 5])
print("---")
print(R)
print("---")
R = np.delete(R, [0, 4])
print("after deleting elements:\n", R)
print("---")

# rank 2 array axis 0 is : row & axis 1 is column
T = np.arange(1, 10).reshape(3,3)
print(T)
T = np.delete(T, 0, axis=0) # delete row 
print("--- delete 1st row --- ")
print(T)
print("--- delete 0,2 column ---")
T = np.delete(T, [0,2], axis=1)
print(T)

# ADDING values using append() : TAKES (3 args) : array + list of elements to append + axis to append on row or column: 
y = np.array([1, 2, 3, 4, 5])
y = np.append(y, 6)
print("--- add element --- ")
print(y)
print("---")
# add more than one element at once : 
y = np.append(y, [7,8])
print(y)

# rank 2 array : 
o = np.arange(1, 10).reshape(3,3)
print(o)
print("--- add row in rank 2 array --- ")
o = np.append(o, [[10, 11, 12]], axis=0)
print(o)
print("---")
u = np.arange(1, 10).reshape(3,3)
print("--- add column in rank 2 array --- ")
u = np.append(u, [[10], [11], [12]], axis=1)
print(u)
print("---")

# insert values into numpy arrays using insert() that takes (4 args) : array + index + element + axis

# rank 1 array : 
p = np.array([1, 2, 5, 6, 7])
print(p)
#insert()
p = np.insert(p, 2, [3,4])
print("--- inserted elements --- ")
print(p)
print("---")

# rank 2 array ADD ROW : 
a = np.array([[1,2,3],[7,8,9]])
a = np.insert(a, 1, [[4, 5, 6]], axis=0 )
print("--- inserted elements --- ")
print(a)
print("---")

# rank 2 array ADD COLUMN : 
d = np.array([[1,2,3],[7,8,9]])
print(d)
d = np.insert(d, 1, 5, axis=1 )
print("--- inserted elements --- ")
print(d)
print("---")