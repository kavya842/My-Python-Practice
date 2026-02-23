# for i in range(1,4):
#     for j in range(1,3):
#         print(i,j)

"""i/p:- s='save the tigers', o/p:-{'save':4,'the':3,'tigers':6}"""
# s='save the tigers'
# a={}
# for i in s.split():
#     count=0
#     for j in i:
#        count+=1
#        a[i]=count
# print(a)
"""Write a program to check whether a number is strong number or not"""
num=int(input())
sum=0
for j in str(num):
    n=int(j)
    fact=1
    for i in range(1,n+1):
        fact*=i
    sum+=fact
print(sum)
if num==sum:
    print('strong number')
else:
    print('not a strong number')