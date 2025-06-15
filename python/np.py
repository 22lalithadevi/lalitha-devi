n=int(input("Enter the value of num: "))
if n>0:
    print(n ," is Positive")
if n<0:
    print(n,"is Negative")
if n==0:
    print(f"{n}Zero")

#terinary operator
result="+ve number" if(n>0) else "-ve number"
print(f"{n} is {result}")