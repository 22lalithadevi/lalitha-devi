n=int(input("enter the value: "))
list=[]
for i in range(n):
    temp=int(input(f"enter the value {i} is: "))
    list.append(temp)
print("user entered list: ",list)
for i in range(n):
    if (list[i]<0):
        list[i]=0
for i in range(n):
    if(list[i]%3==0):
        print(list[i])
print("uptaded list: ",list[i])