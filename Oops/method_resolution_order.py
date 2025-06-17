#this is in the format of hybrid inheritence
class a:
    def myname(self):
        print('im class a')
class b(a):
    def myname(self):
        print('im class b')
class c(a):
    def myname(self):
        print('im class c')
class d(c,b):
    pass
e=d()
print(d.__mro__)               # ans is in tuple format
print(d.mro())                 # ans is in list format
