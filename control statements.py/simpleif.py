"""Write a program to print a number if it is even"""
#n=int(input('enter the number:'))
#if n%2==0:
#    print(n)

"""Write a program to print the square of a number if number is even"""
#n=int(input('enter the value'))
#if n%2==0:
#     print(n**2)

"""Write a program whether the character is vowel"""
#char=(input('enter the char:'))
#if char  in ['a','e','i','o','u']:
#    print(char)

# (or)
#char=input('enter the vowel')
#if char in ('a','e','i','o','u',A','E','I','O','U'):
#    Print('it is a vowel')

"""Write a program to print the ascii value of a char  if char is uppercase"""
#char=input('enter the character:')
#if 65 >= ord(char) <= 90:
#    print('the ascii value of character:',ord(char))
# (or)
#ch=input('enter the char:')
#if 'A'<=ch<='Z':
#   print(ord(ch))

"""Write a program to print cube of a number if it is divisible by 9 and 6"""
#a=int(input('enter the number:'))
#if a %9 == 0 and a %6 == 0:
#    print('the cube number:',a**3)

"Today Assignment 04-02-2026"
#1)Write a program to print last digit of a num if it is 2 digit number 
#num=int(input('enter the number:'))
#if 10<=abs(num)<=99:
#   print(abs(num)%10)
          
                       #output: abs(num)--> converts negative number to positive 
           # example -45 to 45 
           # 10<=abs(num)<=99  checks whether the number is 2 digit 
           #abs(num)%10  gives the last digit 
           #example 45%10=5
           #print()-->prints the last digit
""" Write to check whether a last digit of a num is divisible by 2"""
#num=int(input('enter the number:'))
#if (abs(num)%10)%2==0:
#   print("Divisible by 2")

          #output: 38 % 10 =8 (last_digit) % 2==0 checks if it is even , even number --> divisible by 2 , if condition is true -->prints message

""" write a program to print reverse of a str if it is starting with digit """
s=input('enter a value:')
if s[0].isdigit():
    print(s[::-1])
#output: "1abc"-->"cba1"