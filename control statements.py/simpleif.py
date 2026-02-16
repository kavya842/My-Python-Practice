"""Write a program to print a number if it is even"""
# n=int(input('enter the number:'))
# if n%2==0:
#     print(n)

"""Write a program to print the square of a number if number is even"""
# n=int(input('enter the value'))
# if n%2==0:
#      print(n**2)

"""Write a program whether the character is vowel"""
# char=(input('enter the char:'))
# if char  in ['a','e','i','o','u']:
#     print(char)

# # (or)
# char=input('enter the vowel')
# if char in ('a','e','i','o','u','A','E','I','O','U'):
#     print('it is a vowel')

"""Write a program to print the ascii value of a char  if char is uppercase"""
# char=input('enter the character:')
# if 'A' <= char <= 'Z':
#     print('the ascii value of character:',ord(char))
# # (or)
# ch=input('enter the char:')
# if 'A'<=ch<='Z':
#    print(ord(ch))

"""Write a program to print cube of a number if it is divisible by 9 and 6"""
# a=int(input('enter the number:'))
# if a %9 == 0 and a %6 == 0:
#     print('the cube number:',a**3)

# "Today Assignment 04-02-2026"
# 1)Write a program to print last digit of a num if it is 2 digit number
# num=int(input('enter the number:'))
# if 10<=abs(num)<=99:
#    print(abs(num)%10)

#                     # (or)
#                     #n=int(input('enter the number:'))
#                     #if len(n)==2:
#                     #print('last digit of  2 digit  number:',n[-1])

#            #output: abs(num)--> converts negative number to positive
#            # example -45 to 45
#            # 10<=abs(num)<=99  checks whether the number is 2 digit
#            #abs(num)%10  gives the last digit
#            #example 45%10=5
#            #print()-->prints the last digit

""" Write to check whether a last digit of a num is divisible by 2"""
# num=int(input('enter the number:'))
# if (abs(num)%10)%2==0:
#        print("Divisible by 2")

#           #output: 38 % 10 =8 (last_digit) % 2==0 checks if it is even , even number --> divisible by 2 , if condition is true -->prints message

""" write a program to print reverse of a str if it is starting with digit """
# s=input('enter a string:')
# if s[0].isdigit():
#     print(s[::-1])                 # by using inbuilt functions
# #output: "1abc"-->"cba1"
#            # (or)
# s=input('enter a string:')
# if 48<=ord(s[0])<=57:              # without using inbuilt functions
#     print("reverse the string starting with digit:",s[::-1])
#   #output: 48 means 0 and 57 means 9 ascii values these are 48 and 57

"""06-02-2026"""
"""Write a program to print the uppercase letter and later convert into lower case letter"""
# char=input('enter the character:')
# if  'A'<=char<='Z':
#     print("the letter is in upper case:",ord(char))
#     print("the conversion of upper case letter into lower case letter:",(chr(ord(char)+32)))
#     print('the lower case number:',ord(chr(ord(char)+32)))        #  lower to  upper -32 and upper to lower +32

"""Write  a program to check whether the data is single value data type"""
# n=eval(input('enter the value:'))                                  # n=eval(input('enter any data'))
# if type(n) not in (list,tuple,set,str,dict):              # (or)     if type(n) in (int,float,bool,complex):
#     print('enter the values',type(n))                              # print('it is a single value datatype')


"""Write  a program to check whether the data is mutable"""
# n=eval(input('enter the values'))
# if type(n) in (list,set,dict):
#     print('it is a mutable data types')

""" Write a program to print the given values are default values or not"""
# n=eval(input('enter the data'))                                      data = eval(input('enter the value'))                  n=eval(input('enter the data'))
# if  not bool(n):                                           (or)      if bool(data) is False:               (or)             if bool(n) == False:              (or) if bool(n) not in [True]:
#     print(' default values',bool(type(n)))                            print('default value' )                               print('default value')
