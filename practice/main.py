"""Write a program to print a number if it is even"""
# n=int(input('enter the number:'))
# if n%2==0:
#     print(n)
"""Write a program to print the square of a number if number is even"""
# n=int(input('enter the number:'))
# if n%2==0:
#     print(n**2)
"""Write a program whether the character is vowel"""
# char=input('enter the character:')
# if char in ['a','e','i','o','u']:
#     print(char)
"""Write a program to remove duplicates from a list using comprehension """
# n=[10,20,30,40,50,10,20]
# unique_list=list(set(n))
# print(unique_list)
"""Write a program to remove duplicates from a list using list comprehension without using set() function """
# n=[10,20,30,40,10,20]
# n1=[]
# for i in n:
#     if i not in n1:
#         n1.append(i)
# print(n1)
"""i/p:-'aabcbba output:-a2b1c1b2a1"""
s='aabcbba'
result=''
for i in s:
    count=s.count(i)
    if i not in result:
        result+=i+str(count)
print(result)
