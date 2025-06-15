a=int(input("enter first number= "))
b=int(input("enter second number= "))
temp=0
a=a+b
b=a-b
a=a-b
print("swap numbers: ",a,b)
temp=b
b=a
a=temp
print("n-1: ",b)
print("n-2: ",a)