n=int(input("Emter the value: "))
if (n>-10 and n<10):
    print("Digit")
else:
    print("Number")
#terinay operator
res="Digit" if(n>-10 and n<10) else "Number"
print(f"{n} is {res}")