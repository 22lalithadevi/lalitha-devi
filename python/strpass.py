str=input("enter the password: ")
for ch in str:
    if ch.isalpha():
        if ch.isdigit():
            if ch==['!','@','#','$','%','^','&','*']:
                print("password is valid...!")
else:
    print("password is invalid enter valid password")