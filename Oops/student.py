class student:
    def __init__(self,name,rollno,mat_marks,phy_marks,che_marks):
        self.name=name
        self.rollno=rollno
        self.mat_marks=mat_marks
        self.phy_marks=phy_marks
        self.che_marks=che_marks
class derived(marks):
    def __init__(self,mat_marks,phy_marks,che_marks):
        marks.__init__(self)   
        print(self.mat_marks+phy_marks+che_marks)    