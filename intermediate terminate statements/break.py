"write a program to find prime number or not using break statement"
# n=int(input('enter the number:'))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print('it is not a prime number')
#             break
#     else:
#         print('it is a prime number')
# else:
#     print('it is not a prime number')
#  (or)
# n=5
# for i in range(2,5):
#     if n%i==0:
#         print('it is not a prime number')
#         break
# else:
#     print('it is a prime number')

"""Write a program to find the guess the number """
# n=65
# while True:
#     guess=int(input('enter the guess:'))
#     if guess==n:
#         print('hey your guess is right')
#         break
#     elif guess<n:
#         print('your guess is low')
#     else:
#         print('your guess is high')

"""Write  a program to print elements of a list if you encounter any ofmultiple of  5 and break or stop the iterations"""
# l=[1,2,3,4,5,6,7,8]
# for i in l:
#     if i%5==0:
#         break
#     print(i)
"""Write a program given a string of words create a dictionary where words will be the key and value will be the length of the word but it should not start  with a  word vowel letter"""
s='hello world this is python programming'
d={}
for i in s.split():
    if i[0] not in 'aeiouAEIOU':
        d[i]=len(i)
print(d)



