"""Write a program given a string of words create a dictionary where words will be the key and value will be the length of the word but it should not start  with a  word vowel letter"""
# s='ello world this is python programming'
# d={}
# for i in s.split():
#     if i[0]  in 'aeiouAEIOU':
#         continue                
#     d[i]=len(i)
# print(d)
"""Write a program to print first n palindrome but the palindrome should not divisible by 11 by using continue statement"""
# n=int(input('enter the number:'))
# count=0
# i=1
# while count<n:
#     if str(i)==str(i)[::-1]:
#         if i%11==0:
#             i+=1
#             continue
#         print(i)
#         count+=1
#     i+=1
"""Write a program to take users input untill user enter the correct username:"""
# n='vk'
# while True:
#         n=input('enter the username:')
#         if n=='vk':
#              print('hey your username is correct')
#              break
#         print('hey reenter the username')
"""Write a program to find a first palindrome in a collection of numbers and string"""
# l=[23,11,2,3,4,5,'hello','world','python']
# for i in l:
#     if str(i)==str(i)[::-1]:
#         print(i)
#         break
"""Write  a program to validate the password if the password is contain the 3 special characterrs and 2 numbers and 3 capital letters and password should be less than or equal to 8 and password is combination of all of these"""
# password=input('enter the password:')
# if len(password)>8:
#    s=0
#    c=0
#    d=0
#    for i in password:
#       if i.isupper():
#          c+=1
#       if i.isdigit():
#          d+=1
#       if i in '@#$%^&*':
#          s+=1
#    if s>3 and c>=3 and d>2:
#         print('hey your password is valid')
#    else:
#         print('hey your password is invalid')
# else:
#     print('length is less than 8')
"""Write a program to print n number of prime numbers"""
n=int(input('enter the number:'))
count=0
i=2
while count<n:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        count+=1
    i+=1

# (or in continue keyword)

# n=int(input('enter the number:'))
# count=0
# i=2
# while count<n:
#     for j in range(2,i):
#         if i%j==0:
#             i+=1
#             continue
#     else:
#         print(i)
#         count+=1
#     i+=1


          
    




     

    


