"""Write  a Program to check whether the middle value of list is integer or not """
# l=eval(input('enter the list:'))
# if len(l)%2==1:
#     if type(l[len(l)//2])==int:
#         print(l[len(l)//2])
#     else:
#         print('middle value is not a integer')
# else:
#     print('there is no middle value')

"""Write a program to check whether a charcter is vowel or consonent"""
# n=input('enter the character:')
# if n in ('A','E','I','O','U','a','e','i','o','u'):
#     print('it is a  vowel')
# else:
#     print('it is a character')


"""Write a  program to find the greatest number among 4 numbers using nestedif"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
if a > b:
    if a > c:
        if a > d:
            print("Greatest number is:", a)
        else:
            print("Greatest number is:", d)
    else:
        if c > d:
            print("Greatest number is:", c)
        else:
            print("Greatest number is:", d)
else:
    if b > c:
        if b > d:
            print("Greatest number is:", b)
        else:
            print("Greatest number is:", d)
    else:
        if c > d:
            print("Greatest number is:", c)
        else:
            print("Greatest number is:", d)

