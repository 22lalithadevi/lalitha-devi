from abc import ABC,abstractmethod          #the name of abstract class is car and abstract method is milage
class car(ABC):
    @abstractmethod
    def milage(self):
        pass
class tesla(car):
    def milage(self):
        print('milage is 20kmph')          #if method is overriding then it is dynamic in nature
class ferrari(car):
    def milage(self):
        print('milage is 32kmph')
t1=tesla()
t1.milage()
f1=ferrari()
f1.milage()
