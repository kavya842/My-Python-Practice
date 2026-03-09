# """Write  a program to print the lower primary diagonal pattern"""
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# """Write  a program to print the upper primary diagonal pattern"""
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# """Write  a program to print the primary diagonal pattern"""
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# * 
#    *
#       *
#          *
#             *
"""4) --------------------------------"""
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print('@',end=' ')
#         elif i<j:
#             print('#',end=' ')
#         else:
#             print(' ',end=' ')
#     print()                           
# o/p:-
# @ # # # # 
#   @ # # #
#     @ # #
#       @ #
#         @
# 5)-----------------------------
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print('@',end=' ')
#         elif i<j:
#             print('#',end=' ')
#         else:
#             print('$',end=' ')
#     print()
# 6)----------------------------------
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print('#',end=' ')
#         elif i==n:
#             print('#',end=' ')
#         elif j==1:
#             print('#',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# o/p:-
#
# #
#   #
#     #
# # # # #
# 7)----------------------------
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print('#',end=' ')
#         elif i==1:
#             print('#',end=' ')
#         elif j==n:
#             print('#',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# o/p:- 
# # # # # 
  #     #
    #   #
      # #
        #
# 8)--------------------------------
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print('#',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# o/p:-
# # # # # # 
#         #
#         #
#         #
#         #
# # # # # #
# 9)--------------------------------
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i+j==n+1:
#             print('#',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# o/p:-
#           # 
  #       #
    #   #
      #
    #   #
  #       #
#           #
# 10)----------------------------------
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==(n+1)//2 or j==(n+1)//2:
#             print('#',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=5
# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or j==1 or i==5 or j==5:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

# n=5
# for i in range(1,6):
#     for j in range(1,6):
#         if i==3 or j==3:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#      *     
#     *     
# * * * * *
#     *
#     *

# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==(n+1)//2 or j==(n+2)//2:
#             print('*',end=" ")
#         else:
#             print(' ',end=' ')
#     print()
#       *       
#       *
#       *
# * * * * * * *
#       *
#       *
#       *
# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1:
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print()
#         * 
#       *   (secondary diagonal)
#     *     
#   *       
# *
"""Write a program to print lower secondary diagonal."""
# n=int(input("Enter a num:"))("lower secondary diagonal")
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j>n+1:
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print()

#         * 
#       * *
#     * * *
#   * * * *
"""write a program to print upper secondary diagonal"""
# n=int(input("Enter a num:"))("upper secondary diagonal")
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j<n+1:
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print()

# * * * *   
# * * *
# * *
# *
""""""
# n=11
# for i in range(1,n+1):
#     print("  "*(n-i),end=" ")
#     for j in range(1,(2*i)):
#         if j==1 or j==(2*i -1 ) or i==n:
#             print('*',end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#          * 
#        *   * 
#      *       * 
#    *           *
#  * * * * * * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# *       * 
#   *   *   
#     *
#   *   *
# *       *
# n=int(input("enter a num"))
# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if i==n or i+j==n+1 or j-i==n-1:
#             print('*',end=" ")
#         else:
#             print(" ",end=" ")
#     print() 
# enter a num5
#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *
# n=int(input("enter a num:"))
# for i in range(1,n+1):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
# n=int(input("enter a num:"))
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
#  * * * * * 
#   * * * *
#    * * *
#     * *
#      *
# n=int(input("enter a num"))
# n=5
# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if i==n or i+j==n+1 or j-i==n-1  :
#             print('*',end=" ")
#         else:
#             print(" ",end=" ")
#     for k in range(n,1,-1):
#         if j==n or i+j==n+1 or i-j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print() 
"""n=5
for i  in range(n):
    print(" "* (n-i-1)+"*"* (2*i +1))
for i in range(n,0,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))"""
# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()
"""n=int(input("enter a num:"))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()"""
# n=6
# for i in range(n):
#     print(' '*(n-i-1),end=" ")
#     print("*"*(i+1))
# for i in range(n-2,-1,-1):
#     print(" "*(n-i-1),end=" ")
#     print("*"*(i+1))
"""n=int(input("Enter a num:"))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i,n):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()"""
# Enter a num:5
#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     for j in range(1,n*2):
#         if i+j==n+1 or j-i==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,n*2):
#         if i+j==n+1 or j-i==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     *    
#    * *   
#   *   *  
#  *     * 
# *       *
#  *     * 
#   *   *  
#    * *   
#     *  
"""1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5"""
"""n=int(input("enter a num:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()
enter a num:5
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5"""
"""n=int(input("enter a num:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
enter a num:5
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5"""
# n=int(input("enter a num:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
"""OR"""
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# 1
# 1 2       
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
"""n=int(input("enter a num:"))
for i in range(1,n+1):
    k=i
    for j in range(1,n+1):
            if i>=j:
              print(k,end=" ")
              k+=1
    print()"""
'''n=int(input("enter a num:"))
for i in range(1,n+1):
    k=i
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()'''
"""n=5
for i in range(1,n+1):
    k=5
    for j in range(1,n+1):
        if i+j>=n+1:
            print(k,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
        5 
      5 4 
    5 4 3
  5 4 3 2
5 4 3 2 1"""
"""n=5
for i in range(1,n+1):
    k=5
    for j in range(1,n+1):
        if i<=j:
            print(j,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
1 2 3 4 5 
  2 3 4 5 
    3 4 5
      4 5
        5"""
# n=int(input("enter a num:"))
# a=n%2!=0
# for i in range(1,a):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
"""n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()"""
# n=5
# for i in range(1,n+1):
#     k=65
#     for j in range(1,+i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()
# A 
# A B 
# A B C
# A B C D
# A B C D E
# n=5
# for i in range(1,n+1):
#     k=65
#     for j in range(1,+i+1):
#         if i>=j:
#            print(chr(k),end=" ")
#         k+=1
#     print()



