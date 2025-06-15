n=int(input("enter the value: "))
list=[]
for i in range(1,n+1):
    temp=int(input(f"enter the value {i} is: "))
    list.append(temp)
print("Max number= ",max(list))