# class A:
#     __a=10
#     __b=20
#     def __init__(self,c):
#         self.c=c
#     def __disp(self):
#         print(self.c)
#     @classmethod
#     def __display(cls):
#         print(cls.__a,cls.__b)
#     @staticmethod
#     def __msg():
#         print("public access specifier")
# obj=A(60)
# A.__a=90
# A.__b=12
# obj.__display()
# obj.__disp()
# A.__display()
# obj.__msg()

"""1)syntax method"""
class School:
    __Sname="sri chaitanya"
    __Sloc="JNTU"
    def __init__(self,name):
        self.__name=name
    def __disp(self):
        print(self.__name)
s1=School('Dora')
print(School._School__Sname)
s1._School__disp()
School._School__Sname="narayana"
print(School._School__Sname)

"""getter and setter function"""
class School:
    __Sname="Sri chaitanya"
    __Sloc="jntu"
    def __init__(self,name):
        self.__name=name
    def __disp(self):
        print(self.__name)
    def get_var(self):
        print(self.__name)
    def set_var(self,new):
        self.__name=new
S1=School("dora")
S1.get_var()
S1.set_var('bujji')
S1.get_var()