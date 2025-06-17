class student:
    def __init__(self,name,rollno,mat_marks,phy_marks,che_marks):
        self.name=name
        self.rollno=rollno
        self.mat_marks=mat_marks
        self.phy_marks=phy_marks
        self.che_marks=che_marks
    def cal(self):
        if(self.mat_marks>=40 and self.phy_marks>=40 and self.che_marks>=40):
            total= self.mat_marks+self.phy_marks+self.che_marks
            avg=total/3
            print(total)
            print(avg)
            if(self.mat_marks>75 or self.phy_marks>75) or (self.phy_marks>75 and self.che_marks>75) or (self.che_marks>75 and self.mat_marks>75):
                print("admission is confirmrd..!")
            else:
                print("admission is not confirmrd....!")
s1=student("lalitha",148,99,98,99)
s1.cal()
