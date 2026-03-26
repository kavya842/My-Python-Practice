"""Check the range of numbers even or not"""
# even=lambda n:n%2==0
# even1=map(even,range(1,11))
# print(list(even1))

"""I/p:-['hi','hello'] o/p:- [2,5]"""
# l=['hi','hello','kavya','em chestunav']
# print(list(map(len,l)))

"""s='tomorrow is working day' """
"""O/p:- ['tw','is','wg','dy]"""
# s='tomorrow is working day'
# print(list(map(lambda i:i[0]+i[-1],s.split())))

"""s='tomorrow is working day'"""
"""O/p:-{'tomorrow':'worromot','is':'si','working':'gnikrow','day':'yad'}"""
# s='tomorrow is working day'
# print(dict(map(lambda i:(i,i[::-1]),s.split())))

"""s='tomorrow is working day'"""
"""O/p:-{'tomorrow':'WORROMOT','is':'SI','working':'GNIKROW','day':'YAD'}"""
# s='tomorrow is working day'
# print(dict(map(lambda i:(i,i[::-1].upper()),s.split())))

"""s='tomorrow is working day'"""
"""O/p:-{'tomorrow':'TOMORROW','is':'SI','working':'Working','day':'Yad'}"""
# s='tomorrow is working day kavya'
# print(dict(map(lambda s:(s,s.upper()) if len(s)%2==0 else (s,s.capitalize()) ,s.split())))

"""Write a program to extarct prime numbers from 1 to 20"""

