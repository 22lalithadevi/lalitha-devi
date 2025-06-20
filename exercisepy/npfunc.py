'''import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a)
print(m.sum())
print(a.sum())
print(m.sum(axis=1))
print(a.sum(axis=1))

print(a.max())
print(m.max())
print(a.max(axis=1))
print(m.max(axis=1))
print(a.max(axis=0))
print(m.max(axis=0))

print(a.cumsum())
print(m.cumsum())

print(a.min())
print(m.min())
print(a.min(axis=1))
print(m.min(axis=1))
print(a.min(axis=0))
print(m.min(axis=0))

print(len(a))
print(len(m))

print(a.prod())
print(m.prod())
print(a.prod(axis=1))
print(m.prod(axis=1))
print(a.prod(axis=0))
print(m.prod(axis=0))

#transpose(changing column to row and row to column)
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a.T)
print(m.T)
#or
print(a.transpose())
print(m.transpose())
#trace (is a function if both indexes are same then it is diagnol)
print(a.trace())
print(m.trace())

#unique elements
import numpy as np
a=np.array([[1,1,1],[2,2,2],[3,3,3]])
m=np.matrix('1,1,1;2,2,2;3,3,3')
print(np.unique(a))
print(np.unique(m))

#determinant
import numpy as np
a=np.array([[6,1,1],[4,-2,5],[2,8,7]])
m=np.matrix('6,1,1;4,-2,5;2,8,7')
ans=np.linalg.det(a)
print(ans)
ans1=np.linalg.det(m)
print(ans1)
#mean(average)
ans=a.mean()
ans1=m.mean()
print(ans)
print(ans1)

import numpy as np
a=np.zeros((3,4),dtype=int)
print(a)

import numpy as np
a=np.ones((3,4),dtype=int)
print(a)

import numpy as np
a=np.ones((3,4))
print(a)

import numpy as np
a=np.full((3,4),5)
print(a)

import numpy as np
a=np.array([[1,2,3],[3,6,9],[4,8,12]])
m=np.matrix('2,3,6;3,6,9;4,8,12')
x=np.sort(a,axis=None)
y=np.sort(m,axis=None)
print(x)
print(y)

import numpy as np
a=np.array([[1,2,3],[3,6,9],[4,8,12]])
m=np.matrix('2,3,6;3,6,9;4,8,12')
x=np.sort(a,axis=1)
y=np.sort(m,axis=1)
print(x)
print(y)

#assending order sorting
import numpy as np
a=np.array([[1,2,3],[3,6,9],[4,8,12]])
m=np.matrix('2,3,6;3,6,9;4,8,12')
x=np.sort(a,axis=1)
y=np.sort(m,axis=1)
print(x)
print(y)'''

#descending order
import numpy as np
a=np.array([[1,2,3],[3,6,9],[4,8,12]])
m=np.matrix('2,3,6;3,6,9;4,8,12')
x=(np.sort(-a,axis=1))*-1
y=(np.sort(-m,axis=1))*-1
print(x)
print(y)

import numpy as np
a=np.array([[1,2,3],[3,6,9],[4,8,12]])
m=np.matrix('2,3,6;3,6,9;4,8,12')
x=(np.sort(-a,axis=0))*-1
y=(np.sort(-m,axis=0))*-1
print(x)
print(y)

#addition,substraction,multiplication by using array and matrix
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[4,5,6],[1,2,3]])
c=np.matrix('1,2,3;4,5,6')
d=np.matrix('4,5,6;1,2,3')
ans=np.sum([a,b],axis=1)
print(ans)
ans1=np.sum([c,d],axis=1)
print(ans1)

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[4,5,6],[1,2,3]])
c=np.matrix('1,2,3;4,5,6')
d=np.matrix('4,5,6;1,2,3')
ans=np.diff([a,b],axis=1)
print(ans)
ans1=np.diff([c,d],axis=1)
print(ans1)

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,0],[0,1],[1,0]])
c=np.matrix('1,2,3;4,5,6')
d=np.matrix('1,0;0,1;1,0')
ans=a.dot(b)
print(ans)
ans1=c.dot(d)
print(ans1)

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,0,1],[0,1,0],[1,0,1]])
print(a*b)