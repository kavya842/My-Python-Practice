"""Write a program to print the sum of even numbers in a list"""
# def add(a,sum=0):
#  for i in a:
#     if i%2==0:
#         sum=sum+i
#  print(sum)
# add([2,3,4])

# (or)

# def add(l,sum=0):
#     for i in l:
#         if type(i)==int:
#             if i%2==0:
#                 sum+=i
#     print(sum)
# add([2,3,4,5,6,'hello'])

"""i/p:- ['a','b','c'][10,20,30] o/p:- {'a':10,'b':20,'c':30}"""
# def dict(keys,values, d={}):
#     if len(keys)==len(values):
#         for i in range(len(keys)):
#             d[keys[i]]=values[i]
#     print(d)
# dict(['a','b','c'], [10,20,30])
"""i/p:- 'Belated happy holi'o/p:- 'detaleb yppah iloh"""
# def rev(s):
#     words=s.split()
#     a=[]
#     for i in words:
#         a.append(i[::-1])
#     b=" ".join(a)
#     print(a)
# rev("belated happy birthday")