size=int(input("enter length of list: "))
list=[]
for i in range(size):
    temp=int(input(f"enter the value {i} is: "))
    list.append(temp)
print("before reversing list: ",list)
print("reversed list: ",list[::-1])