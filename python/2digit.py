n=int(input("Emter the value: "))
if (n<=-10 and n>100 or n>=10 and n<100):
    print("Two Digit")
else:
    print("Not a digit")
#terinay operator
res="Two Digit" if(n<=-10 and n>100 or n>=10 and n<100) else "Not a digit"
print(f"{n} is {res}")