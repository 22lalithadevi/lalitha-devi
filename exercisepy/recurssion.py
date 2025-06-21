'''a=int(input())
b=int(input())
for i in range(a,b+1):
    print(i)


#recursive low to high
def rlh(x,y):
    if x<=y:
        print(x)
        x+=1
        rlh(x,y)                #recursive calling function
a,b=map(int,input().split())
rlh(a,b)

#recursive high to low
def rhl(x,y):
    if x>=y:
        print(x)
        x-=1
        rhl(x,y)                #recursive calling function
a,b=map(int,input().split())
rhl(a,b)

#to print factorial of given number
def fact(y):
    f=1
    for i in range(1,y+1):
        f=f*i
    print(f)       
a=int(input())
fact(a)

#or
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1) 
n=int(input())
f=fact(n)
print(f)

#recursion fact for 5 to 1
def fact(n,a,b):
    if (n==a):
        print(b)
    else:
        n-=1
        return fact(n,a,b*n) 
n=int(input())
if (n==1 or n==0):
        print(1)
else:
    f=fact(n,1,n)

#to find GCD(hcf) of given num
import math
print(math.gcd(5,12))
print(math.lcm(5,12))

#gcd using nonrecursion(using loops)
a,b=map(int,input().split)
while a!=b:
    print(a,b)
    if a>b:
        a=a-b
    else:
        b=b-a
print(a)
print(b)

#gcd recursion (using loops)
def rgcd(a,b):
    if(a==b):
        return a
    if(a>b):
        return rgcd(a-b,b)
    else:
        return rgcd(a,b-a)
a,b=map(int,input().split())
ans=rgcd(a,b)
print(ans)'''

#lcm using recursion
def rlcm(a,b,x,y):
    if(a==b):
        return (x*y)//a
    if(a>b):
        return rlcm(a-b,b,x,y)
    else:
        return rlcm(a,b-a,x,y)
a,b=map(int,input().split())
ans=rlcm(a,b,a,b)
print(ans)