class a:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):            #operator overloading is performing by function overloading
        return self.a+o.a
ob1=a(1)
ob2=a(2)
print(ob1+ob2)
ob3=a('geeks')
ob4=a('for')
print(ob3+ob4)
