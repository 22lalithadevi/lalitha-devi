n=int(input("Emter the value: "))
if (n<=-100 and n>1000 or n>=100 and n<1000):
    print("Three Digit")
elif (n<=-1000 and n>10000 or n>=1000 and n<10000):
    print("Four Digit")
else:
    print("Not a Three or Four digit")