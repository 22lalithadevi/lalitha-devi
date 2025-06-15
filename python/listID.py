sample_id=input("enter the lab sample id: ")
nid=int(input("enter the no of IDs you have to generate:"))
list=[]
for i in range(1,nid+1):
    if sample_id.isalnum():
        sample_format=(sample_id+1)
        list.append(i)
    print(list)