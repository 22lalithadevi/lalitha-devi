"""import numpy as np
x=np.array([1,2,3,4,5])
print(x)
x+=2
print(x)

#type
import numpy as np
x=np.array([1,2,3,4,5])
print(x.dtype)

#universal datatype
import numpy as np
x=np.array([1,2,3,4,5.5,'abc'])
print(x.dtype)

#no of dimention datatype
import numpy as np
x=np.array([1,2,3,4,5])
print(x.ndim)

#size
import numpy as np
x=np.array([1,2,3,4,5])
print(x.size)

'''import numpy as np
x=np.array([1,2],[3,4,5])
print(x.shape)'''

n=int(input('enter a value: '))
x=np.ndarray(shape=n,dtype=int)
for i in range(n):
    v=int(input())
    x[i]=v
print(x)

#print odd and even values
n=int(input('enter a value: '))
x=np.ndarray(shape=n,dtype=int)
for i in range(n):
    v=int(input())
    x[i]=v
print(x)
ans=np.where(x%2==0)
print(ans)
tot=np.where(x%2!=0)
print(tot)

#print indexes for the particular given data
import numpy as np
n=int(input('enter a value: '))
x=np.ndarray(shape=n,dtype=int)
for i in range(n):
    v=int(input())
    x[i]=v
print(x)
k=int(input())
ans=np.where(x==k)
print(ans)

import numpy as np
n=int(input('enter a value: '))
x=np.ndarray(shape=n,dtype=int)
for i in range(n):
    v=int(input())
    x[i]=v
print(x)
k=int(input())
ans=np.where(x>k)
print(ans)"""
'''
#find the index of new insert number
import numpy as np
n=int(input('enter a value: '))
a=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    x=int(input())
    a[i]=x
print(a)
d=int(input('enter new value: '))
ans=np.searchsorted(a,d)
print(a)
print('position for new number: ',ans)


#data sorting
import numpy as np
n=int(input('enter a value: '))
a=np.ndarray(shape=(n),dtype=int)
for i in range(n):
    x=int(input())
    a[i]=x
print(a)
a.sort()
print(a)


#2d array
import numpy as np
x=([1,2,3],[4,5,6],[7,8,9])
a=np.array(x)
print(a)
print(a.dtype)
print(a.shape)
print(a.ndim)
print(a.size)

#to print in a single line
import numpy as np
x=([1,2,3],[4,5,6],[7,8,9])
a=np.array(x)
print(a)
print(*a)

#using for loop
import numpy as np
x=([1,2,3],[4,5,6],[7,8,9])
a=np.array(x)
for i in a:
    print(i)


#using range
import numpy as np
x=([1,2,3],[4,5,6],[7,8,9])
a=np.array(x)
for i in range(3):
    for j in range(3):
        print(a[i][j],end=' ')       #by using this we can remove brackets
    print()


#to print elements with their indexes
import numpy as np
x=([1,2,3],[4,5,6],[7,8,9])
a=np.array(x)
for i in range(3):
    for j in range(3):
        print(a[i][j],(i,j),end=' ')       
    print()


#matrix
import numpy as np
x=([1,2,3],[4,5,6],[7,8,9])
a=np.matrix(x)
print(a)
print(a.dtype)


import numpy as np
x=([1,2,3],[4,5,6],[7,8,9])
a=np.matrix(x)
m=np.array(x)
print(a)
ans=a.flatten()
print(ans)
ans1=m.flatten()
print(ans1)


x=([1,2,3],[4,5,6])
m=np.matrix(x)
a=np.array(x)
a1=a.reshape(3,2)
print(a1)
m1=m.reshape(3,2)
print(m1)'''


#arthmatic operations
import numpy as np
x=([1,2,3],[4,5,6],[7,8,9])
b=np.matrix(x)
a=np.array(x)
a=a+1
print(a)
b=b-1
print(b)
a=a*2
print(a)
b=b%2
print(b)
a=a/2
print(a)
b=b//2
print(b)