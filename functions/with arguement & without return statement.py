"""Write a program to print the sum of even numbers in a list"""
def add(a,sum=0):
 for i in a:
    if i%2==0:
        sum=sum+i
 print(sum)
add([2,3,4])