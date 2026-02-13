"""Write a program to check whether the character is special character or not"""

# ch=input('enter the value:')                                                  ch=input('enter the value:')
# ascii_val=ord(ch)                                                             if not ('a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'):
# if not  ((ascii_val >= 65 and ascii_val <= 90) or                                  print('It is a special characetr:')
#         (ascii_val >= 97 and ascii_val <= 122) or                 (or)        else:
#         (ascii_val >= 48 and ascii_val <= 57)):                                    print('It is not a special character:')
#     print('it is a special character')
# else:
#     print('it is not a special character')

"""Write  a program to check whether a string is keyword or not"""
# n=input('enter the keyword:')
# import keyword
# if n in (keyword.kwlist):                       //manam import statement program starting lo import chayali//
#     print('it is a keyword')
# else:
#     print('it is not a keyword')

"""Write a program to check whether a string is having length is 5 and ending with uppercase """
# n=input('enter the string:')
# if len(n)==5 and 'A'<=n[-1]<='Z':
#     print('it is a string with len5 and ending with uppercase')
# else:
#     print('it is not string with len 5 and not ending with uppercase')

 # or
# n=input('enter the string:')
# if len(n)==5 and 'a'<=n[-1]<='z':
#     print('it is a string with len5 and ending with lowercase')
# else:
#     print('it is not string with len 5 and not ending with lowercase')

"""Write a program to check whether the string is palindrom or not"""
# n=input('enter the string:')
# if n[::1]==n[::-1]:
#     print('it is a palindrom')
# else:
#     print('it is not a palindrom')

"""Write a program TO reverse starting with uppercase  ending with lowercase and middle character is a digit"""
# n=input('enter the character:')
# mid = len(n)// 2
# if len(n)>=3 and 'A'<=n[0]<='Z' and '0'<=n[mid]<='9' and 'a'<=n[len(n)-1]<='z':
#     print('it satifies')
#     # rev=n[len(n)-1]+n[mid]+n[0]  
#     rev=n[::-1]
#     print('reversed',rev)
# else:
#     print('it does not satifies')

"""Write a program to check whether a number is positive or negitive"""
# n=int(input())
# if n>=0:
#      print('it is a positive number')
# else:
#     print('it is not a positive number')

"""Write  a program to check whether middle value of list is integer or not """

# l=eval(input('enter the list:'))
# # l=[10,20,30,40,50]
# mid=len(l)//2
# if type(l[mid])==int:
#     print('integer')
# else:
#     print('not integer')


"""Write a program to check whether a collection is homogenous or not """
# l = eval(input("Enter collection: "))
# if type(l[0]) == type(l[1]) and type(l[1]) == type(l[2]):                  (or)       if type(l[0])==type(l[-1]):
#     print("Homogeneous")
# else:
#     print("Not Homogeneous")

