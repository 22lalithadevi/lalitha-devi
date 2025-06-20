'''list1=['boe','batch','of','2023']
str1='@#'
print(str1.join(list1))'''


#example  Vignan College Bt @ 2025
s=input('enter string: ')
uc=lc=di=sc=0
for i in s:
    if i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
    elif i.isdigit():
        di+=1
    else:
        sc+=1
print('upper count: ',uc)
print('lower count: ',lc)
print('digit count: ',di)
print('special character count: ',sc)
