def arthmatic(a,b):
    c=a+b
    d=a-b
    x=a*b
    z=a%b
    e=a/b
    y=a//b
    print(c,d,x,z,e,y)
arthmatic(4,9)

#with return
def arthmatic(a,b):
    c=a+b
    d=a-b
    x=a*b
    z=a%b
    e=a/b
    y=a//b
    return(c,d,x,z,e,y)

res=arthmatic(4,6)
print(res)