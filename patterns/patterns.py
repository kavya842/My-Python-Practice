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




