def is_prime(num):
    count=0
    for i in range(1,num+1):
        if(num%1==0):
            count+=1
    if(count==2):
        print(num,'is prime')
    else:
        print(num,'is not prime')
is_prime(14)
is_prime(9)
is_prime(45)

def is_prime(num):
    count=0
    if num>0:
        for i in range(2,num//2+1):
            if(num%i==0):
                count+=1
        if(count==0):
            print(num,'is prime')
    else:
        print(num,'is not prime')
num=int(input('enter num: '))
is_prime(num)