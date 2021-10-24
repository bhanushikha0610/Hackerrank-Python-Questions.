#!/usr/bin/env python
# coding: utf-8

# ## Zeros and Ones

# In[ ]:


import numpy
import numpy
num=tuple(map(int, input().split()))
print(numpy.zeros(num, dtype=numpy.int))
print(numpy.ones(num, dtype=numpy.int))


# ## Eye and Identity

# In[ ]:


import numpy
numpy.set_printoptions(legacy='1.13')
n,m=map(int, input().split())
print(numpy.eye(n,m, k=0))


# ## Array Mathematics2

# In[ ]:


import numpy
n,m=map(int, input().split())
a=numpy.array([list(map(int, input().split())) for _ in range(n)])
b=numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))


# ## Floor, Ceil and Rint

# In[ ]:


import numpy
numpy.set_printoptions(legacy='1.13')
a=tuple(map(float, input().split()))
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


# ## Sum and Prod

# In[ ]:


import numpy
n,m=map(int, input().split())
a= numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(a, axis=0), axis=0))


# ## Min and Max

# In[ ]:


import numpy

N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(storage, axis=1), axis=0))


# ## Mean, Var, and Std

# In[ ]:


import numpy

N,M = map(int, input().split())
l = []

for i in range(N):
    a = list(map(int, input().split()))
    l.append(a)

l = numpy.array(l)

numpy.set_printoptions(legacy='1.13')
print(numpy.mean(l, axis = 1))
print(numpy.var(l, axis = 0))
print(numpy.std(l))


# ## Dot and Cross

# In[ ]:


import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))


# ## Inner and Outer

# In[ ]:


import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A, B), numpy.outer(A, B), sep='\n')


# ## Polynomials

# In[ ]:


import numpy

poly = [float(x) for x in input().split()]
x = float(input())

print(numpy.polyval(poly, x))


# ## Linear Algebra

# In[ ]:


import numpy
N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)
print(round(numpy.linalg.det(A),2))


# ## Transpose and Flatten

# In[ ]:


import numpy
n, m = map(int, input().split())

storage = numpy.array([input().strip().split() for _ in range(n)], int)
print (storage.transpose())
print (storage.flatten())


# ## shape and reshape

# In[ ]:


import numpy
# Shape and Reshape in Python - Hacker Rank Solution START
print(numpy.array(input().split(), int).reshape(3, 3))


# ## Arrays

# In[ ]:


def arrays(arr):
   #revrser array first, convert to float array with numpy
   return(numpy.array(arr[::-1], float))


# In[ ]:





# In[ ]:




