"""Write a  program to check whether the given character is special charactor or not"""
special =lambda s:s  not in (('A'<=s<='Z')  or s not in ('0'<=s<='9'))
print(special(','))
# (or)

"""Write a program to check whether the given character is vowel or not"""
# vowel=lambda ch:ch in 'aeiouAEIOU'
# print(vowel('k'))

"""Write a program to check whether the given starting the uppercase or not"""
# upper=lambda ch: ch[0].isupper()
# print(upper('Hello'))

"""Write to program to check whether the given value is default value or not"""
# default =lambda v:not bool(v)
# print(default([]))

"""Write a program to perform addition between minimum 3 and maximum 6"""
# add=lambda a,b,c,d=0,e=0,f=0:a+b+c+d+e+f
# print(add(1,2,3))

"""Write a program to convert the character into uppercase after each and every special character"""
# convert=lambda ch: ch.title()
# print(convert('he#jkuy%a'))

"""Write a program to check whether a word is keyword is not"""
# import keyword
# check=lambda k: 'keyword' if  k  in keyword.kwlist else ' not keyword'
# print(check('True'))

"""Write a program to check a string is palindrome or not and it should be middlecharacter should be uppercase"""
# palindrome=lambda s:'palindrome' if s==s[::-1]  and s[len//2] else 'not a palindrome'
# print(palindrome('KaVya'))

"""Write a program to check whether the last digit is even or not"""
# check=lambda d:'even' if abs(d)%10%2==0 else 'not even'
# print(check(24))