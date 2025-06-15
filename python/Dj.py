size=int(input("enter length of list: "))
DJ_list=[]
unique_list=[]
for i in range(size):
    temp=input(f"enter the value {i} is: ")
    DJ_list.append(temp)
print("songs in normal order: ")
print(DJ_list)
print("songs in reverse order: ")
print(DJ_list[::-1])