str1=input("enter the first string: ")
str2=input("enter the second string: ")
list=[]
if len(str1)!=len(str2):
    print("Error..!give both sequences in same length")
else:
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            list.append(i)
    print(list)