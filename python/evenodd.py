n=int(input("enter the value: "))
even_list=[]
odd_list=[]
for i in range(1,n+1,2):
    odd_list.append(i)
for i in range(2,n+1,2):
    even_list.append(i)
print("even list: ",even_list)
print("odd list: ",odd_list)