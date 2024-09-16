import numpy as np 
# create Rank 1 array : 
x = np.array([1, 2, 3, 4, 5])
import numpy as np
print(np.__version__)
print(x)
print(type(x))
print("number of Dimentions: ", x.ndim)

# create Rank 2 array : 
y = np.array([[1,2,3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("Array: ",y)
print("Shape: ", y.shape)
print("size: ", y.size)
print("dtype: ", y.dtype)
print("type: ", type(y))
print("number of Dimentions: ", y.ndim)

# save numPy array to a file: 
# the file created automatically in .npy extention 
try: 
    np.save("my_array", y)
    print("ndarray saved successfully!")

except: 
    print("ERROR!")

# load the saved array: 
z = np.load("my_array.npy")
print(" z array = ", z)

# create ndarray using built in functions: (FULL OF ZEROS)
n = np.zeros((3, 4))
print(n)
# create ndarray using built in functions: (FULL OF ONES)
f = np.ones((3, 4))
print(f)
# create ndarray full of same number  
m = np.ones((3,2))
print(m)
print('m has dimensions:', m.shape)
print('m is an object of type:', type(m))
print('The elements in m are of type:', m.dtype) 
# create square Identity Matrix N x N ndarray: 
print("Eye N x N ndarray: ")
c = np.eye(3)
print(c)
# create a 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50
k = np.diag([10,20,30,50])
print()
print('k = \n', k)
print()

# create a rank 1 ndarray that has sequential integers from 0 to 9
o = np.arange(10)
# print the ndarray
print()
print('o = ', o)
print()

# print information about the ndarray
print('o has dimensions:', o.shape)
print('o is an object of type:', type(o))
print('The elements in o are of type:', o.dtype) 
print()

# create a rank 1 ndarray that has evenly spaced integers from 1 to 13 in steps of 3.
e = np.arange(1,14,3)

# print the ndarray
print()
print('e = ', e)
print()

# print information about the ndarray
print('e has dimensions:', e.shape)
print('e is an object of type:', type(e))
print('The elements in e are of type:', e.dtype) 

# create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.
l = np.linspace(0,25,10)

# print the ndarray
print()
print('l = \n', l)
print()
# np.linspace(0,25,10) returns an ndarray with 10 evenly spaced numbers in the closed interval [0, 25]

# print information about the ndarray
print('l has dimensions:', l.shape)
print('l is an object of type:', type(l))
print('The elements in l are of type:', l.dtype) 

# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25,
# with 25 excluded.
x = np.linspace(0,25,10, endpoint = False)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 

# We create a rank 1 ndarray with sequential integers from 0 to 19
x = np.arange(20)

# We print x
print()
print('Original x = ', x)
print()

# We reshape x into a 4 x 5 ndarray 
x = np.reshape(x, (4,5))

# We print the reshaped x
print()
print('Reshaped x = \n', x)
print()

# We print information about the reshaped x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 

# We create a a rank 1 ndarray with sequential integers from 0 to 19 and
# reshape it to a 4 x 5 array 
Y = np.arange(20).reshape(4, 5)

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype) 

# We create a 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
r = np.random.random((3,3))

# We print r
print()
print('r = \n', r)
print()

# We print information about r
print('r has dimensions:', r.shape)
print('r is an object of type:', type(r))
print('The elements in r are of type:', r.dtype)

# We create a 3 x 2 ndarray with random integers in the half-open interval [4, 15).
X = np.random.randint(4,15,size=(3,2))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)


# We create a 1000 x 1000 ndarray of random floats drawn from normal (Gaussian) distribution
# with a mean of zero and a standard deviation of 0.1.
X = np.random.normal(0, 0.1, size=(1000,1000))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
print('The elements in X have a mean of:', X.mean())
print('The maximum value in X is:', X.max())
print('The minimum value in X is:', X.min())
print('X has', (X < 0).sum(), 'negative numbers')
print('X has', (X > 0).sum(), 'positive numbers')