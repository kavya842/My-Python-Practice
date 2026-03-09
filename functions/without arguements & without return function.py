"""Write a program with using without arguements and without return statement"""
# def rev():
#     s=eval(input('enter the collection:'))
#     if type(s) in [str,list,tuple]:
#         print(s[::-1])
#     else:
#         print('enter the collection which supports indexing')
# rev()

"""Write a program to count the no.of uppercase char and no.of lowercase char and special char in a str"""
# def count():
#     s=eval(input('enter the string:'))
#     spe=0
#     upper=0
#     lower=0
#     for i in s:
#         if i.isupper():
#             upper+=1
#         elif i.islower():
#             lower+=1
#         elif i.isalpha():
#             spe+=1
#     print(spe)
#     print(upper)
#     print(lower)
# count()
"""i/p:- 'hum apke hai kon' o/p:- 'kon hai apke hum' """
# def rev():
#     n=eval(input('enter the string:')).split()
#     b=" ".join(n[::-1])
#     print(f"'{b}'")
# rev()
"""Write a function to concatinate two lists  without + operator """
# def concat():
#     n=eval(input())
#     n1=eval(input())
#     for i in n1:
#        n.append(i)
#     print(n)
# concat()

# (or)

# def concat():
#     n=eval(input())
#     n1=eval(input())
#     n.extend(n1)
#     print(n)
# concat()