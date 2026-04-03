""" we can create our own custom error by declaring a class
    which inherits exception class and then we can raise that error using raise keyword"""
class BestFriend(Exception):
    def __init__(self,message):
        super().__init__(message)
balance=1000
amount=100
if balance<amount:
    raise BestFriend('insuffienct balance')
else:
    print("successfully withdrawn")