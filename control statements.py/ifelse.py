"""Write a program to check whether the character is special character or not"""

# ch=input('enter the value:')                                                  ch=input('enter the value:')
# ascii_val=ord(ch)                                                             if not ('a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9'):
# if not  ((ascii_val >= 65 and ascii_val <= 90) or                                  print('It is a special characetr:')
#         (ascii_val >= 97 and ascii_val <= 122) or                 (or)        else:
#         (ascii_val >= 48 and ascii_val <= 57)):                                    print('It is not a special character:')
#     print('it is a special character')
# else:
#     print('it is not a special character')