# class A:
#     def __init__(self,a):
#         self.a=a
# obj1=A(10)
# obj2=A(20)
# print(obj1+obj2)


"""With magic words"""
class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        self.a+other.a
        return self.a*other.a 
obj1=A(10)
obj2=A(20)
print(obj1+obj2)