""" class method :-- Class method is a method that works on class variables 
                     and is used to access or modify the common data shared by all objects of a class."""
class fest:
    festname="MIC FEST"
    collegename="DVR&Dr.HS MIC COLLEGE OF TECHNOLOGY"
    festdate="18-3-2026"
    def __init__(cls,studentname,rollno,branch,address,eventname):
        cls.studentname=studentname
        cls.rollno=rollno
        cls.branch=branch
        cls.address=address
        cls.eventname=eventname
    def disp(cls):
        print(cls.studentname,cls.rollno,cls.branch,cls.address,cls.eventname,fest.festname)
    @classmethod
    def change_festname(cls,micfesto):
        cls.festname = micfesto
    def change_studentname(self,newname):
        self.studentname=newname
student1=fest("tarak","IT",1260,"hyd","web wizards")
student2=fest("showrya","CSE",1109,"ongole","paper presentation")
print("before change")
student1.disp()
student2.disp()
print(vars(student1))
print(vars(student2))

fest.change_festname("mictech fest 2026")
student1.change_studentname('mani')
student2.change_studentname('kavya')

print("after change")
student1.disp()
student2.disp()
print(vars(student1))
print(vars(student2))
           