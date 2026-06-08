class PythonFullstack:
    def __init__(self):
        self.pfs_students = []
    def add_pfs(self,*student):
        self.pfs_students.extend(student)
    def display_PFS(self):
        print("Python full stack students:")
        print(self.pfs_students)
class Javafullstack:
    def __init__(self):
        self.jfs_students=[]
    def add_jfs(self,*student):
        self.jfs_students.extend(student)
    def display_jfs(self):
        print("Java full stack students:")
        print(self.jfs_students)
class Datascience:
    def __init__(self):
        self.ds_students = []
    def add_ds(self,*student):
        self.ds_students.extend(student)
    def display_ds(self):
        print("Datascience students:")
        print(self.ds_students)
class Datanalytics:
    def __init__(self):
        self.da_students = []
    def add_da(self,*student):
        self.da_students.extend(student)
    def display_da(self):
        print("Data analytics students:")
        print(self.da_students)
class Testing:
    def __init__(self):
        self.ts_students = []
    def add_ts(self,*student):
        self.ts_students.extend(student)
    def display_ts(self):
        print("Testing students:")
        print(self.ts_students)
class PythonCourse(PythonFullstack, Javafullstack, Datascience, Datanalytics, Testing):
    def __init__(self):
        PythonFullstack.__init__(self)
        Javafullstack.__init__(self)
        Datascience.__init__(self)
        Datanalytics.__init__(self)
        Testing.__init__(self)

    def disp_python(self):
        self.display_PFS()
        self.display_jfs()
        self.display_ds()
        self.display_da()
        self.display_ts()
s1 = PythonCourse()
s1.add_pfs("dora",8919951981,"ramya",9652738424,"surya",7671071426)
s1.add_jfs("siva",1234567897,"ravi",9987654321)
s1.add_ds("sravani","sravan","stayam")
s1.add_da("pavani","pravathi","devi")
s1.add_ts("lucky","gagan","raju")
s1.disp_python()