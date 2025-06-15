n=int(input("Enter month number:"))
if (n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12):
    print("NO.of days=31")
elif(n==4 or n==6 or n==9 or n==11): 
    print("No.of days=30")
elif(n==2):
    print("No of days are 28 or 29")
else:
    print("In-valid month number")