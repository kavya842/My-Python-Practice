class A:
    __a=10
    __b=20
    def __init__(self,c):
        self.c=c
    def __disp(self):
        print(self.c)
    @classmethod
    def __display(cls):
        print(cls.__a,cls.__b)
    @staticmethod
    def __msg():
        print("public access specifier")
obj=A(60)
A.__a=90
A.__b=12
obj.__display()
obj.__disp()
A.__display()
obj.__msg()