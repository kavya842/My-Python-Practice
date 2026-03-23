class Fullstack:
    def __init__(self):
        self.fs_students = []
    def add_fs(self,*name):
        self.fs_students.extend(name)
    def display_FS(self):
        print("Full stack students:")
        print(self.fs_students)
class Datascience:
    def __init__(self):
        self.ds_students = []
    def add_ds(self,*name):
        self.ds_students.extend(name)
    def display_ds(self):
        print("Datascience students:")
        print(self.ds_students)
class Datanalytics:
    def __init__(self):
        self.da_students = []
    def add_da(self,*name):
        self.da_students.extend(name)
    def display_da(self):
        print("Data analytics students:")
        print(self.da_students)
class Testing:
    def __init__(self):
        self.ts_students = []
    def add_ts(self,*name):
        self.ts_students.extend(name)
    def display_ts(self):
        print("Testing students:")
        print(self.ts_students)
class PythonCourse(Fullstack, Datascience, Datanalytics, Testing):
    def __init__(self):
        Fullstack.__init__(self)
        Datascience.__init__(self)
        Datanalytics.__init__(self)
        Testing.__init__(self)

    def disp_python(self):
        self.display_FS()
        self.display_ds()
        self.display_da()
        self.display_ts()
s1 = PythonCourse()
s1.add_fs("dora","ramya","surya")
s1.add_ds("sravani","sravan","stayam")
s1.add_da("pavani","pravathi","devi")
s1.add_ts("lucky","gagan","raju")
s1.disp_python()