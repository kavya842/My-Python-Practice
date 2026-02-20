"""Write a program to print numbers from 10 to 1"""
# for i in range(10,0,-1):
#     print(i)
"""Write a program to print odd numbers"""
# for i in range(1,20,2):
#     print(i)
"""write a program to print even numbers"""
# for i in range(0,20,2):
#     print(i)
"""Write a program to print characters present at even index"""
# ch=eval(input())
# for i in range(len(ch)):
#     if i%2==0:
#      print(ch[i])
# (or)
# ch=eval(input())
# for i in range(0,len(ch),2):
#     print(ch[i])
"""Write a program to find the length of the collection without using len()"""
# ch=eval(input())
# count=0
# for i in ch:
#     count+=1
# print(count)
"""Assignment Questions"""
"""Write a program the lowercase char if its ascii value is even"""
# s=eval(input())
# for i in s:
#     if i.islower():
#         if ord(i)%2==0:
#             print(i)

# (0r)
# s=eval(input())
# for i in s:
#     if 'a'<=i<='z':
#         if ord(i)%2==0:
#            print(i)
"""Write  a program the sum of integers in present a  set """
# s=eval(input())
# sum=0
# for i in s:
#     sum=sum+i
# print(sum)
#  (or)
# s=eval(input())
# sum=0
# for i in s:
#     if type(i)==int or type(i)==float:
#         sum=sum+i
# print(sum)
"""Write a program to display the split of string and its length"""
# s=input().split()
# a=[]
# for i in s:
#    a.append((i,len(i)))
# print(a)
"""Write a program to reverse the string"""
# i/p:-'sunday is funday'
# o/p:-{'sunday','yadnus','is','si','funday','yadnuf'}
# s='sunday is funday'.split()
# a={}
# for i in s:
#    a[i]=i[::-1]
# print(a)

# (or)

# s='sunday is funday'.split()
# a={}
# for i in s:
#     a.setdefault(i,i[::-1])
# print(a)

"""Write a program to find out """
# i/p:-'hyderabad is famous for chicken biriyani'
# o/p:-{'hyderabad','r','is','is','famous','fs','for','o','chicken','c','biriyani','bi'}
# n=input() .split()
# a={}
# for i in n:
#      if len(i)%2==0:
#           a[i]=i[0]+i[-1]
#      else:
#           a[i]=i[len(i)//2]
# print(a)
"""Write a program to find the occurance of a specified character in a string """
n='kavya'
n1='v'
count=0
for i in n:
    if i==n1:
        count+=1
print(count)

           