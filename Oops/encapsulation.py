#encapsulation 'security'
class base:
    def __init__(self):
        self.__a=32          #private data attribute
        print(self.__a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self.__a+2)
#b1=derived()         # this will give error because it is prive we can only use withih a function
b1=base()             #this will print 32
