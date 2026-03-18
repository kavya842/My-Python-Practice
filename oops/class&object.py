"""Creating class and object"""
# class institute:
#     institutename="Jspiders"
#     address="hyderabad"
#     founder="kavya"
#     contactno=9876567879

# student1=institute()

# student1.name="kavya"
# student1.fathername="ravikumar"
# student1.phno=98787847728
# student1.address="ongole"
# student1.course="pythonfullstack"

# student2=institute()

# student2.name="mani"
# student2.fathername="Ravi"
# student2.phno=98787847787
# student2.address="ongole"
# student2.course="Javafullstack"

# print(student1.name, student1.fathername,student1.phno,student1.address,student1.course)
# print(student2.name, student2.fathername,student2.phno,student2.address,student2.course)

""" using constructor / __init__/ initialization method  """
# class institute:
#     institutename="jspiders"
#     address="hydjntu"
#     founder="kavya"
#     contactno=9878786543
#     def __init__(self,name,fathername,phno,address,course):
#         self.name=name
#         self.fathername=fathername
#         self.phno=phno
#         self.address=address
#         self.course=course 
# student1=institute("kavya","ravikumar",8919951981,"ongole","pythonfullstack")
# student2=institute("mani","ravikumar",8919951976,"ongole","javafullstack")
# print(student1.name,student1.fathername,student1.phno,student1.address,student1.course)
# print(student2.name,student2.fathername,student2.phno,student2.address,student2.course)

"""user defined method"""
# class institute:
#     institutename="jspiders"
#     address="hydjntu"
#     founder="kavya"
#     contactno=9878786543
#     def __init__(self,name,fathername,phno,address,course):
#         self.name=name
#         self.fathername=fathername
#         self.phno=phno
#         self.address=address
#         self.course=course
#     def disp(self):
#         print(self.name,self.fathername,self.phno,self.address,self.course)
# student1=institute("kavya","Ravikumar",8919951981,"ongole","pythonfullstack")
# student2=institute("mani","Ravikumar",8919951976,"ongole","javafullstack")
# student1.disp()
# student2.disp()
# print(vars(student1))
# print(vars(student2))
# print(dir(institute))

"""Modify two values of an object"""
class panchayat:
    wardno=10
    panchayatname="kamepalli"
    panchayatloc="kamepalli"
    def __init__(self,name,fathername,village,panchayatname,wardno):
        self.name=name
        self.fathername=fathername
        self.village=village
        self.panchayatname=panchayatname
        self.wardno=wardno
    def disp(self):
        print(self.name,self.fathername,self.village,self.panchayatname,self.wardno)
    def old(self,addr):
        self.village=addr
    def new(self,addr):
        self.village=addr
people1=panchayat("kavya",  "ravikumar",   "kamepalli",  "kamepalli", 10)
people2=panchayat("mani",    "ravi",        "kamepalli",  "kamepalli", 12)
people1.disp() 
people2.disp()
people1.old('miyapur')
people1.disp()

# print(vars(people1))
# print(vars(people2))
# print(dir(panchayat))