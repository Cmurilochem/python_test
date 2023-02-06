import numpy as np
import matplotlib.pyplot as plt

i=0
nmax=100

#for i in range(nmax):
#    x[i] = float(i)+1.0
#    print(x[i])

x = np.array([float(n+1) for n in range(nmax)])

y = np.array([float(n+1) for n in range(nmax)])

z_dot = np.dot(x,y) # dot product

z = x*y # product of each component

print(
    x,
    x.size, # size of the array
    x.ndim, # dimension
    x.shape, # shape
    z_dot,
    z
    )    

# using now some universal functions

x = np.linspace(0,2*np.pi,num=10)
y = np.sin(x)

print(x,y.mean(),y.max())

#plt.plot(x,y)
#plt.show()

x_2D = np.array([ [1,2,3],[4,5,6],[7,8,9] ])

print(x_2D)

c = x_2D[0][0:3:2] # in the row zero, give me the 0, 1, 2 elements in steps of 2 

print(c)

c = x_2D[0:3][2] # give only last row

print(c)

### universal functions again

A = np.array([[1,0],[0,1]])
B = np.array([[1,2],[2,0]])

print(np.dot(A,B),np.matmul(A,B))