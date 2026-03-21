class school:
    students="students"
    faculty="faculty"
    def __init__(self,studentname,facultyname,classroomno,subject):
        self.studentname=studentname
        self.facultyname=facultyname
        self.classroomno=classroomno
        self.subject=subject
    def disp(self):
        print(self.studentname,self.facultyname,self.classroomno,self.subject)
class school_sports(school):
    def __init__(self,studentname,facultyname,classroomno,subject,khokho,kabaddi,running,throwball):
        super(). __init__(studentname,facultyname,classroomno,subject)
        self.khokho=khokho
        self.kabaddi=kabaddi
        self.running=running
        self.throwball=throwball
    def displ(self):
        super().disp()
        print(self.khokho,self.kabaddi,self.running,self.throwball)
class school_cultures(school):
    def __init__(self,studentname,facultyname,classroomno,subject,danceprogram,singingcompetition,drama):
        super(). __init__(studentname,facultyname,classroomno,subject)
        self.danceprogram=danceprogram
        self.singingcompetition=singingcompetition
        self.drama=drama
    def displa(self):
        super().disp()
        print(self.studentname,self.facultyname,self.classroomno,self.subject,self.danceprogram,self.singingcompetition,self.drama)
class school_prizes(school):
    def __init__(self,studentname,facultyname,classroomno,subject,Firstprize,Secondprize):
        super(). __init__(studentname,facultyname,classroomno,subject)
        self.Firstprize=Firstprize
        self.Secondprize=Secondprize
    def display(self):
        super().disp()
        print(self.Firstprize,self.Secondprize)
k1=school_prizes("kavya","ravi",31,"python","Firstprize","Secondprize")
k1.display()
