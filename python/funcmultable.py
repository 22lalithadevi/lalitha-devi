def mul_table(num):
    i=1
    while(i<=10):
        #if(i%num==0 or i%num!=0):
            print(num,'x',i,'=',num*i)
    i+=1
num=int(input("enter a number: "))
mul_table(num)