#issubclass method
class cal1:
    def sum(self,a,b):
        return a+b;
class cal2:
    def mul(self,a,b):
        return a*b;
class derived(cal1,cal2):
    def divide(self, a,b):
        return a/b;
a=derived()
print(issubclass(derived,cal1))
print(issubclass(derived,cal2))
print(issubclass(cal2,cal1))

#isinstance method
class cal1:
    def sum(self,a,b):
        return a+b;
class cal2:
    def mul(self,a,b):
        return a*b;
class derived(cal1,cal2):
    def divide(self, a,b):
        return a/b;
d=derived()
print(isinstance(d,derived))
print(isinstance(d,cal1))
print(isinstance(d,cal2))