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
# if 'a'<=n<='z' or 'A'<=n<='Z':
#    if n in ('A','E','I','O','U','a','e','i','o','u'):
#     print('it is a  vowel')
#    else:
#     print('it is a character')
# else:
#   print('not a  aplhabet')


"""Write a  program to find the greatest number among 4 numbers using nestedif"""
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# if a > b:
#     if a > c:
#         if a > d:
#             print("Greatest number is:", a)
#         else:
#             print("Greatest number is:", d)
#     else:
#         if c > d:
#             print("Greatest number is:", c)
#         else:
#             print("Greatest number is:", d)
# else:
#     if b > c:
#         if b > d:
#             print("Greatest number is:", b)
#         else:
#             print("Greatest number is:", d)
#     else:
#         if c > d:
#             print("Greatest number is:", c)
#         else:
#             print("Greatest number is:", d)

"""Write a  program to login into the instagram by entering the username and password(you should ask the password only when user name is correct)"""
# username='Kavya1260'
# password='8919951981'
# u=eval(input('enter the username:'))
# if u == username:
#      p=eval(input('enter the password:'))
#      if p == (password):
#         print('correct:')
#      else:
#         print('invalid password:')
# else:
#      print('invalid username:')

"""Write a program to print the last value of a list if it is palindrome string ending with vowel"""
# l=eval(input('enter the list:'))
# if type(l[-1])==str:
#     if l[-1]==l[-1][::-1]:
#            if l[-1][-1] in 'aeiouAEIOU':
#                 print(l[-1])
#            else:
#                print('not ending with a vowel')
#     else:
#         print('not a palindrome')
# else:
#     print('not a string')


"""Write a Program to reverse the string if it is starting with vowel and ending with consonent and having a middle value"""
# ch=input('enter the character:')
# if len(ch)%2==1:
#      if ch[0] in 'aeiouAEIOU':
#         if ch[-1] not in 'aeiouAEIOU' and ch[-1].isaplha():
#             print(ch[::-1])
#         else:
#             print('the ending char is not consonent')
#      else:
#         print('the starting char is not vowel')
# else:
#     print('it is not a string')

"""Write a program to find the second greatest number among 4 numbers"""
# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# c = int(input("Enter the number: "))
# d = int(input("Enter the number: "))

# nums = [a, b, c, d]

# nums.sort(reverse=True)

# print("Second greatest number is:", nums[1])

                                                                 #(or)
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# # Step 1 : Find greatest number
# if a >= b and a >= c and a >= d:
    
#     # Step 2 : Find second greatest among remaining (b,c,d)
#     if b >= c and b >= d:
#         second = b
#     elif c >= b and c >= d:
#         second = c
#     else:
#         second = d

# elif b >= a and b >= c and b >= d:
    
#     # Find second greatest among (a,c,d)
#     if a >= c and a >= d:
#         second = a
#     elif c >= a and c >= d:
#         second = c
#     else:
#         second = d

# elif c >= a and c >= b and c >= d:
    
#     # Find second greatest among (a,b,d)
#     if a >= b and a >= d:
#         second = a
#     elif b >= a and b >= d:
#         second = b
#     else:
#         second = d

# else:
    
#     # d is greatest → find second among (a,b,c)
#     if a >= b and a >= c:
#         second = a
#     elif b >= a and b >= c:
#         second = b
#     else:
#         second = c

# print("Second greatest number is:", second)
"""Write  a program to find lowest numbers among the numbers"""
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if a <= b and a <= c and a <= d:
#     lowest = a

# elif b <= a and b <= c and b <= d:
#     lowest = b

# elif c <= a and c <= b and c <= d:
#     lowest = c

# else:
#     lowest = d

# print("Lowest number is:", lowest)

#(or)
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if a <= b:
#     if a <= c:
#         if a <= d:
#             lowest = a
#         else:
#             lowest = d
#     else:
#         if c <= d:
#             lowest = c
#         else:
#             lowest = d
# else:
#     if b <= c:
#         if b <= d:
#             lowest = b
#         else:
#             lowest = d
#     else:
#         if c <= d:
#             lowest = c
#         else:
#             lowest = d

# print("Lowest number is:", lowest)