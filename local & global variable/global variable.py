# def outer():
#     global x
#     x+=10
#     print(x)
# x=10
# outer()
# print(x)
# x+=1
# print(x)
"""Write a program to print power of 2 or not"""
def power_of(n):
    if n&(n-1)==0:
        print('power of 2')
    else:
        print('not a power of 2')
power_of(2**10000)