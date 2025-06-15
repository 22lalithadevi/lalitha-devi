str=input("enter the string: ")
upcount=0
locount=0
consonants=0
for ch in str:
    if str.isalpha():
        if ch in ['a','e','i','o','u']:
            locount+=1
        elif ch in ['A','E','I','O','U']:
            upcount+=1
        else:
            consonants+=1

print("lower count: ",locount)
print("upper count: ",upcount)
print("consonants count: ",consonants)