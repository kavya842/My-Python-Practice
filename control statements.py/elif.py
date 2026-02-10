"""Write a program to check whether a char is uppercase or lowercase or digit"""
# ch=input('enter the character:')
# if  'A'<=ch<='Z':
#     print('It is a uppercase character')
# elif  'a'<=ch<='z':
#     print('It is a lowercase character')
# else:
#     print('it is a digit')

"""Write a program to check whether number is single digit , double digit, triple digit or more than triple digit"""
n=int(input('enter the number:'))
if 1<=n<=9:
    print('it is a single digit')
elif 10<=n<=99:
    print('it is a double digit')
elif 100<=n<=999:
    print('it is a triple digit')
else:
    print('more than triple digit')