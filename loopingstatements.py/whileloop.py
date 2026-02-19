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

"""Assignment"""
"""Write a program to extract special characters from a string"""
# s = input("Enter a string: ")
# i = 0
# special = ""
# while i < len(s):
#     ch = s[i]
#     if not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9')):
#         special = special + ch
#     i += 1
# print("Special characters:", special)

"""Write a program to extract the integers from the list"""
# lst=eval(input('enter the list'))
# i=0
# a=[]
# while i<len(lst):
#     if type(lst[i])==int:
#         a.append(lst[i])
#     i+=1
# print(a)

# """write a program to check whether a number is perfect number or not """ perfect number means sum of the factors of the number itself
# n=int(input('enter the number'))
# i=1
# a=0
# while i<n:
#      if n%i==0:
#           a=a+i
#      i=i+1
# print(a)
# if a==n:
#      print("perfect number")
# else:
#      print("Not a perfect number")
"""Write a program to reverse  a integer"""
# n=int(input('enter the number:'))
# rev=0
# while n > 0 :
#     lastdigit=n%10
#     rev=rev*10+lastdigit
#     n=n//10
# print(rev)
"""Write a program to reverse a string without slicing"""
# str=eval(input('enter the string'))
# i=len(str)-1
# rev=""
# while i>=0:  
#     rev=rev+str[i]
#     i=i-1
# print(rev)

#  (or)

# a=input('enter the string')
# b=0
# rev=''
# while b<len(a):
#     rev=a[b]+rev
#     i=i+1
# print(rev)

"""Write a  program to print sum of the digits of the number"""
# n=int(input('enter the number:'))
# a=0
# while n>0:
#     a+= n%10
#     n= n//10
# print(a)

"""Write a program to print whether the number armstrong or not"""
# n=int(input('enter the number:'))
# temp=n
# s=0
# while n>0:
#     d=n%10
#     s=s+d**3
#     n=n//10
# if temp==s:
#     print('it is a armstrong')
# else:
#     print('it is not a armstrong')
# (or)
# n=int(input('enter the number:'))
# count=0
# sum=0
# temp=n
# temp1=n
# while temp>0:
#     count+=1
#     temp=temp//10
# while temp1>0:
#     k=temp%10
#     sum+=k**count
#     temp1=temp1//10
# if n==sum:
#     print(f'it is a armstrong number')
# else:
#     print(f'it is a armstrong number')


"""Write a program to print a  number is palindrome or not"""
# n=int(input('enter the numebr:'))
# temp=n
# a=0
# while n>0:
#     d=n%10
#     a=a*10+d
#     n=n//10
# if temp==a:
#     print('it is a palindrome')
# else:
#     print('it is not a palindrome')
"""Write a program to count the no.of digits present in a number without using len()"""
# n=int(input('enter the number:'))
# i=0
# while n>0:
#     n%10
#     n=n//10
#     i+=1
# print(i)
# (or)
# a=int(input('enter the number:'))
# count=0
# while a>0:
#     count+=1
#     a=a//10
# print(count)
"""Write a program to remove the duplicates from a list"""
# l=eval(input())
# i=0
# lst1=[]
# while i<len(l):
#    if l[i] not in lst1:
#       lst1+=[l[i]]
#    i+=1
# print(lst1)
"""Write a program to find the greatest number from the list"""
# n=eval(input())
# i=0
# n1=[0,]
# while i<len(n):
#     if n[i]>n1[0]:
#         n1.pop()
#         n1+=[n[i]]
#     i+=1
# print(n1)

# (or)
# n=eval(input())
# i=0
# largest=0
# while i<len(n):
#     if n[i]>largest:
#         largest=n[i]
#     i+=1
# print(largest)

"""Write a program to check whether the number is prime number or not"""
# n = int(input())
# i = 2
# while i < n and n % i != 0:
#     i += 1
# if i == n and n > 1:
#     print("prime")
# else:
#     print("not prime")
"""Write a program to replace the space in a str with ** """ 
# i/p:hello world
# o/p:hello**world
s=eval(input('enter the string'))
o=" "
i=0
while i<len(s):
    if s[i]==" ":
        o=o+"**"
    else:
        o=o+s[i]
    i+=1
print(o)