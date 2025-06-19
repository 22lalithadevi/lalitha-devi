'''import numpy as np
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

import numpy as np
x=np.array([1,2],[3,4,5])
print(x.shape)

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
print(ans)'''

import numpy as np
n=int(input('enter a value: '))
x=np.ndarray(shape=n,dtype=int)
for i in range(n):
    v=int(input())
    x[i]=v
print(x)
k=int(input())
ans=np.where(x>k)
print(ans)