seq=input("enter your sequence: ")
Acount=0
Tcount=0
Ccount=0
Gcount=0
for i in seq.upper():
    if i=='A':
        Acount+=1
    elif i=='T':
        Tcount+=1
    elif i=='G':
        Gcount+=1
    elif i=='C':
        Ccount+=1
dict={"A":Acount,"T":Tcount,"G":Gcount,"C":Acount}
print(dict)