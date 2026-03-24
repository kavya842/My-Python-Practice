class A:
    _a=10
    _b=20
    def __init__(self,c):
        self.c=c
    def _disp(self):
        print(self.c)
    @classmethod
    def _display(cls):
        print(cls._a,cls._b)
    @staticmethod
    def _msg():
        print("public access specifier")
obj=A(60)
A._a=90
A._b=12
obj._display()
obj._disp()
A._display()
obj._msg()