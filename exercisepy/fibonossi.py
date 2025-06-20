n=int(input('enter a value: '))
a=0
b=1
print(a)
print(b)
for i in range(a,n+1):
    temp=a+b
    a=b
    b=temp
    print(b)
