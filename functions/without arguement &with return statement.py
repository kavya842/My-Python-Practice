"""Write a program to reverse the list or tuple or str"""
# def rev():
#     s=eval(input('enter the collection:'))
#     if type(s) in (str,list,tuple):
#         return(s[::-1])
#     else:
#         return "valid collection"
# print(rev())
"""i/p:- 'hello' o/p:- i want that first l index """
# def ind():
#     s=input('enter the str:')
#     ch=input('enter the char:')
#     for i in range(len(s)):
#         if s[i]==ch:
#             return i
# print(ind())
"""write a  program to extract negitive numbers from a list of integers """
# def extract():
#     s=eval(input('enter the collection:'))
#     a=[]
#     for i in s:
#         if i<0:
#           a.append(i)
#     return a
# print(extract())
"""ASSIGNMENT """
"""Write a program to extract the palindrome string for a list of values and should start with vowels and middle character should be digit """
# def extract():
#     s = eval(input("enter the list: "))
#     a = []
#     for i in s:
#         if type(i) == str:
#             if i == i[::-1]: 
#                 if i[0].lower() in "aeiou":
#                     mid = len(i)//2
#                     if i[mid].isdigit(): 
#                         a.append(i)
#     return a
# print(extract())