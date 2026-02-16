# Step 1️ Identify start value
# Numbers → i = 1
# String → i = 0
# List → i = 0

# Step 2️ Write condition
# Numbers → i <= n
# String → i < len(str)
# List → i < len(list)

# Step 3️ Write logic inside loop
# print / sum / check / multiply

# Step 4️ Increment
# i += 1

"""Write a program to print 10 to 1 numbers"""
# i=10
# while i>=1:
#     print(i)
#     i-=1
"""Write a program to print 1 to n """
# n=int(input('enter the number:'))
# i=1
# while i<=n:
#     print(i)
#     i+=1
"""Write a program to print even numbers from 1 to n"""
# n=int(input('enter the number:'))
# i=1
# while (i<=n):
#     if i%2==0:
#       print(i)
#     i+=1
"""Write a program to print multiplication table of a digit"""
# n=int(input('enter the digit:'))
# i=1
# while (i<=10):
#      print(f'{n}*{i}={i*n}')
#      i+=1
"""Write a  program to print factors of a number"""
# n=int(input('enter the digit:'))
# i=1
# while(i<=n):
#     if n%i==0:
#       print(i)
#     i+=1

"""Write  a program to find the sum of n natural numbers"""
# n=int(input('enter the number:'))
# i=1
# a=0
# while i<=n:
#     a+=i
#     i+=1
# print(a)

"""Write  a program to find the sum of n natural numbers in each and every iteration"""
# n=int(input('enter the number:'))
# i=1
# a=0
# while i<=n:
#     a+=i
#     i+=1
#     print(a)
   
"""Write a program to find the factorial of a number"""
# n=int(input('enter the number:'))         n=int(input('enter the number:))
# i=1                                       fact=1
# a=1                                       while n>=1:
# while i<=n:            (or)                       fact*=n:
#     a*=i                                          n-=1
#     i+=1                                  print(fact)
# print(a)

"""Write a  program to print all the characters from a string"""
# n=input(enter string:')
# i=0
# while i<len(n):
#     print(n[i])
#     i+=1

"""Write  a program to print the vowels present in a string """
# n=input('enter the string:')
# i=0
# k=''
# v=['a','e','i','o','u','A','E','I','O','U']
# while i<len(n):
#     if n[i] in v:
#       k+=n[i]
#     i+=1
# print(k)

"""Write a program to toggle the string"""
# n = input('enter the string')
# i = 0
# k = ""
# while i < len(n):
#     if 'A' <= n[i] <= 'Z':
#         k = k + chr(ord(n[i]) + 32)    
#     elif 'a' <= n[i] <= 'z':
#         k = k + chr(ord(n[i]) - 32)    
#     elif '0' <= n[i] <= '9':
#         k = k + n[i]
#     else:
#         k = k + n[i]
#     i += 1

# print(k)


"""Write a program to extract special characters from a string"""
s = input("Enter a string: ")
i = 0
special = ""
while i < len(s):
    ch = s[i]
    if not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9')):
        special = special + ch
    i += 1
print("Special characters:", special)

"""Write a program to extract the integers from the list"""