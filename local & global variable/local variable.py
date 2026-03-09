# def outer():
#     y=10
#     print(y) # success
# outer()
# print(y) # error 
"""Write a program to print n  number of perfect numbers or 5th perfect number"""
# def perfect(n):
#     res=0
#     for i in range(1,n):
#         if n%i==0:
#             res+=1
#     return res==n
# print(perfect(10))


"""Write a program to check whether the given number is even or not"""
# n=12
# print(n%2==0)

# n=13
# print(n%2==0)
"""Write a program to check whether the given number is odd or not"""
# n=13
# print(n%2==1)
"""Write a program to  print whether the number is palindrome or not"""
# def palin(n):
#     temp = n
#     a = 0
#     while n > 0:
#         d = n % 10
#         a = a * 10 + d
#         n = n // 10

#     if temp == a:
#         return "it is a palindrome"
#     else:
#         return "it is not a palindrome"

# print(palin(121))
# print(palin(122))

# (or)

# def ispal(n):
#     n=str(n)
#     return n==n[::-1]
# ispal(101)
"""Write  a function to check a number is prime or not """
# def check_prime(n):
#     if n <= 1:
#         print("Not a Prime Number")
#         return
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not a Prime Number")
#             return
#     print("Prime Number")
# num = int(input("Enter a number: "))
# check_prime(num)
"""Write  a function to check a number is prime or not from range 1 to 10 """
# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# for i in range(2, 100):
#     if i > 1 and prime(i):
#         print(i)
"""Write a function to create frequency a count """
# a='hello this is'
# def fre(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# print(fre(a))

# (or)

# a='hello this is'
# def fre(s):
#     d={}
#     for i in s.split():
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# print(fre(a))

"""Write a program to check whether the password is valid or not how much username and password will be matching  """
# u=input('enter username:')
# p=input('enter the password:')
# i=0
# fcount=0
# while i<len(u):
#     if len(p)>i and u[i]==p[i]:
#         fcount+=1
#     i+=1
# per = fcount*100 // len(u)
# if per > 70:
#     print('it is not a good password')
# elif per > 40:
#     print('it is average password')
# else:
#     print('it is a strong password')
"""Write a  program to print the sum of first n even numbers using functions"""
# def sum_even(n):
#     s = 0
#     for i in range(1, n+1):
#         s = s + (2*i)
#     print("Sum of first ", n, "even numbers is:", s)
# n = int(input("Enter n value: "))
# sum_even(n)
# (or)
# n=4
# print(n*(n+1))
# (or)
# n=100
# print(n*(n+1)//2)
"""Write a function to calculate the gcd"""
# def gcd(a,b):
#     if b==0:
#         return a 
#     return gcd(b,a%b)
    
# print(gcd(10,20))

# (or)

# def gcd(a,b):
#     res=1
#     for i in range(1,a+1):
#         if a%i==0 and b%i==0:
#             res=i
#     return res
# print(gcd(10,20))


