size=int(input("enter length of list: "))
list=[]
unique_list=[]
for i in range(size):
    temp=int(input(f"enter the value {i} is: "))
    list.append(temp)
print("user entered list: ",list)
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print("unique list: ",unique_list)