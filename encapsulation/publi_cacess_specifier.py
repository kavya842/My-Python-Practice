class A:
    a=10
    b=20
    def __init__(self,c):
        self.c=c
    def disp(self):
        print(self.c)
    @classmethod
    def display(cls):
        print(cls.a,cls.b)
    @staticmethod
    def msg():
        print("public access specifier")
obj=A(60)
A.a=90
obj.display()
obj.disp()
A.display()
obj.msg()