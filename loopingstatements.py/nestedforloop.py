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
# num=int(input())
# sum=0
# for j in str(num):
#     n=int(j)
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     sum+=fact
# print(sum)
# if num==sum:
#     print('strong number')
# else:
#     print('not a strong number')
"""i/p:-'programming is easy' p/p:-{'programming':'oai','is':'i','easy':'ea'}"""
# s='programming is easy'.split()
# a={}
# for i in s:
#     v=''
#     for j in i:
#         if j in 'aeiouAEIOU':
#             v+=j
#     a[i]=v
# print(a)
"""i/p:-[15,10,25,30] o/p:-[65,70,55,50]"""
# l=[15,10,25,30]
# a=[]
# for i in l:
#     sum=0
#     for j in l:
#         sum+=j
#     sum-=i
#     a.append(sum)
# print(a)
"""i/p:-a[100,300,400,700,600] o/p:-[[100,600],[[300,400],[700]]]"""
n=[100,300,400,700,600]
d=[]
for i in n:
   for j in n:
      if i+j==700:
         if [i,j] and [j,i] not in d:
            d.append([i,j])
      elif i==j==700:
         d.append([i])
print(d)