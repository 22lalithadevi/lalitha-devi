n=int(input())
list=[]
for i in range(n):
    A=input()
    list.append(A) 
    l=list[:3]+list[-3:]
print(l)