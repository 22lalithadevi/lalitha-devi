#decimal to binary and binary to decimal
n=int(input('enter num:'))
x=bin(n)
print(x)
print(type(x))
x=x[2:]                   #its present or not but output is same
print(x)
d=int(x,2)                #data to convert, base of convert
print(d)


#decimal to octal and octal to decimal
n=int(input('enter num: '))
x=oct(n)
print(x)
print(type(x))
print(x)
d=int(x,8)                #data to convert, base of convert
print(d)

#decimal to hexadecimal and hexa decimal to decimal
n=int(input('enter num: '))
x=hex(n)
print(x)
print(type(x))
print(x)
d=int(x,16)                #data to convert, base of convert
print(d)