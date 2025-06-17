
#using static method
class maths:
    def addnum(x,y):
        return x+y
m=staticmethod(maths.addnum)
print(m(55,8))


#using decorate 
class physics:
    @staticmethod
    def addnum(x,y):
        return x+y
print(physics.addnum(4,44))
