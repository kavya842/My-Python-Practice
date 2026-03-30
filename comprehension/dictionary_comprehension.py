# d={'ice cream':50,'chocolate':198,'biscuit':25,'cake':450,'lays':59}
# print({i:d[i] for i in d if d[i]>100})
# print({i:d[i] for i in d if d[i]<100})

# s='sunday is working day'
# """o/p:- {'sunday':'SUNDAY','is':'IS','working':'gnikrow,'day':'yad'}"""
# print({i:i.upper() if len(i)%2==0 else i[::-1] for i in s.split()})

"""I/p:- {'dessert':['vanila','chocolate','butterscoth']'starters':['croll','proll'],'main course':['cb','mb']}"""
d={'dessert':['vanila','chocolate','butterscoth'],'starters':['croll','proll'],'main course':['cb','mb']}
print([(i,j) for i in d for j in d[i]])