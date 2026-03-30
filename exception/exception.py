# try:
#     a=int(input("enter the number:"))
#     b=int(input('enter the number:'))
#     print(a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number by zero")
# except ValueError:
#     print("you cannot enter a string value")
# except Exception as e:
#     print("an error occurred:",e)



try:
    print('hello good moening to everyone:!!!')
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print(a/b)
except Exception as e:
    print("an error occurred:",e)
else:
    print("the division is successful")
finally:
    print("the program is executed successfully")