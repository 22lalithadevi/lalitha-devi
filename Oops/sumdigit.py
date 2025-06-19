#sum of given number
n=int(input('enter a number: '))
c=0
while n!=0:
    r=n%10
    c+=r
    #print(c)         #for step ans
    n=n//10
print(c)


#sum of inivisual digits of given num until ans gets in a single digit
n=int(input('enter a number: '))
sum=0
while n!=0:
    r=n%10
    sum+=r
    n=n//10
    if n==0 and sum>9:
        n=sum
        sum=0
print(sum)