class customer:
    def __init__(self,name,items):
        self.name=name
        self.items=items
    def cal(self):
        x=self.items
        total=0
        for i in range(x):
            p=int(input(f'enter price of {i} item: '))
            total+=p
        return total
name=input('enter customer name: ')
items=int(input('enter number of items: '))       
c1=customer(name,items)
total=c1.cal()
if (total>200):
    print('your discount amount for above 200rs is: ',total-total*0.2)
else:
    print('your total amount is: ',total)
