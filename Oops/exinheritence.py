#single level inheritence
class institute:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class branch(institute):
    def __init__(self, name):
        self.name=name
    def show1(self):
        print(self.name)
x=institute('vignan university')
x.show()
y=branch('biotechnology')
y.show1()  
y.show()            #child can use parent data
'''x.show1()            #parent cannot use the child data'''


# another example
class base:
    def __init__(self):
        self._a=22
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self)    #invoking
        print(self._a+2)
x=base()
y=derived()
print(x._a)         #public and protected data can be used anywhere
print(y._a)         #inheritence proof statement 


#multilevel inheritence
class base:
    def __init__(self):
        self._a=35
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self)    #invoking
        print(self._a+2)
class derived1(derived):
    def __init__(self):
        derived.__init__(self)
        print(self._a%2)
x=derived1()

#multiple inheritence
class university:
    uniname=''
    def University(self):
        print(self.uniname)          #default constructor is present
class domain:
    domainname=''
    def Domain(self):
        print(self.domainname)
class branch1(university,domain):
    branch1name=''
    def branch1information(self):
        print(self.uniname)
        print(self.domainname)
        print(self.branch1name)
s1=branch1()
s1.branch1name='vignan university'
s1.uniname='Btech'
s1.domainname='biotechnology'
s1.branch1information()


#hierarchical and hybrid inheritance
class father:
    fathername=''
    def Father(self):
        print(self.fathername)          #default constructor is present
class mother:
    mothername=''
    def Mother(self):
        print(self.mothername)
class Son1(father,mother):
    son1name=''
    def son1information(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)
class Son2(mother):
    son2name=''
    def son2information(self):
        print(self.mothername)
        print(self.son2name)
s1=Son1()
s1.son1name='lalitha devi'
s1.fathername='durga prasad'
s1.mothername='lakshmi chaitanya'
s1.son1information()
s2=Son2()
s2.son2name='sandeep'
s2.mothername='lakshmi chaitanya'
s2.son2information()