class grandfather():
    def show(self):
        print('this is grand father data')
class father(grandfather):
    def show1(self):
        print('this is fathers data')
class son(father):
    def show2(self):
        print('this is sons data')
s1=son()
s1.show()
s1.show1()
s1.show2()

#example with peapock
class dance:
    def dancing(self):
        print('i can dance..!')
class fly:
    def flying(self):
        print('i can fly..!')
class peacock(dance,fly):
    def sound(self):
        print('i can also hum good music...!')
p1=peacock()
p1.dancing()
p1.flying()
p1.sound()
