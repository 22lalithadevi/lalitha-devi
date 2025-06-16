#by using construction
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person('lalitha',20)
p2=person('farheen',21)
print(p1.name,p1.age)
print(p2.name,p2.age)


#without constructor
class person:
    name='lalitha'
    age=20
    print(name,age)
person()

class person:
    name=''
    age=''
p1=person()
p1.name='lalitha devi'
p1.age='20'
print(p1.name,p1.age)

#by using normal method 
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printing(self):
        print(self.name,self.age)
p1=person('lalitha',20)
p2=person('farheen',21)
p1.printing()
p2.printing()

#check wheter a person is major or minor
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printing(self):
        print(self.name,self.age)
    def decide(self):
        if self.age<18:
            print('minor')
        if self.age>=18:
            print('major')
    def upper(self):
        print(self.name.upper())
    def lower(self):
        print(self.name.lower())
    def length(self):
        print(len(self.name))   
p1=person('lalitha',17)
p2=person('farheen',21)
p1.printing()
p2.printing()
p1.decide()
p2.decide()
p1.upper()
p2.upper()
p1.length()
p2.length()