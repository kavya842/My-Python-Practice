# num=int(input('enter the number:'))
# rev=0
# while num>0:
#     ld=num%10
#     rev=rev*10+ld
#     rev//=10
# print(rev) 

# (convert the above the program of while loop into recursive)
# def rev11(num,rev=0):
#     if num<=0:
#         return rev
#     ld=num%10
#     rev=rev*10+ld
#     return rev11(num//10,rev)
# print(rev11(12))

"""i/p:- 3 and o/p:- 32123"""
# def sam(n):
#     print(n,end='')
#     if n==1:
#         return
#     sam(n-1)
#     print(n,end='')
# sam(3)
"""Write a program to find the fibonacci series"""
n=int(input('enter the number:'))
a=0
b=1
while n>0:
    print(a,end='')
    a,b=b,a+b
    n-=1
