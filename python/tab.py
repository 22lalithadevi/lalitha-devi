n=int(input("enter the value: "))
a=10
for i in range(1,a+1):
    if (n%i==0 or n%i!=0):
        print(n,'X',i,'=',n*i)
    i=i+1