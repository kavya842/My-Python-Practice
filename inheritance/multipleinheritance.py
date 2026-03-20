class Add:
    def add(self,a,b):
        self.a=a
        self.b=b
        print(f'the addition of {a} and {b} is:{a+b}')
class Sub:
    def sub(self,a,b):
        self.a=a
        self.b=b
        print(f'the addition of {a} and {b} is:{a-b}')
class Mul:
    def mul(self,a,b):
        self.a=a
        self.b=b
        print(f'the addition of {a} and {b} is:{a*b}')
class Div:
    def div(self,a,b):
        self.a=a
        self.b=b
        print(f'the addition of {a} and {b} is:{a/b}')
class Cal(Add,Sub,Mul,Div):
    def msg(self):
        print('all operations are done')
obj=Cal()
obj.add(8,9)
obj.sub(40,20)
obj.mul(7,3)
obj.div(5,2)
obj.msg()
""" By using pass"""
class Add:
    def add(self,a,b):
        self.a=a
        self.b=b
        print(f'the addition of {a} and {b} is:{a+b}')
class Sub:
    def sub(self,a,b):
        self.a=a
        self.b=b
        print(f'the addition of {a} and {b} is:{a-b}')
class Mul:
    def mul(self,a,b):
        self.a=a
        self.b=b
        print(f'the addition of {a} and {b} is:{a*b}')
class Div:
    def div(self,a,b):
        self.a=a
        self.b=b
        print(f'the addition of {a} and {b} is:{a/b}')
class Cal(Add,Sub,Mul,Div):
     pass
obj=Cal()
obj.add(8,9)
obj.sub(40,20)
obj.mul(7,3)
obj.div(5,2)


class Bank:
    def __init__(self,name):
        self.name=name
    def disp(self):
        print(self.name)
class B(Bank):
    # def __init__(self,age):
    #     self.age=age
    def msg(self):
        print('hello')
cus1=B('dora')
cus1.disp()
cus1.msg()

""" syntax:- class_name.__init__(self) by using this we can do the project of institue management project"""