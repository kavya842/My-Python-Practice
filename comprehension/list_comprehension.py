"""I/p:- ['hello.py','hi.txt','google.com']"""
"""O/p:- l1=[hello,hi,google]
         l2=[py,txt,com]      """
# l=['hello.py','hi.txt','google.com']
# print([i.split('.')[0] for i in l])
# print([i.split('.')[1] for i in l])

"""i/p:-l=['roses','doctor','apple','beautiful']"""
"""O/p:-[('roses',5),('doctor',6),('apple',5),('beautiful',9)]"""
# l=['roses','doctor','apple','beautiful']
# print([(i,len(i)) for i in l])

"""i/p:- [1,2,3,4,5]"""
"""o/p:- [1,2,9,64,625]"""
# print([j**i for i,j in enumerate(range(1,6))])

"""i/p:-['python','hello','php','ruby','aws','pakoda']"""
"""o/p:-['python','php','pakoda]"""
# l=['python','hello','php','ruby','aws','Pakoda']
# print([i for i in l if i[0] in 'pP'])

"""Write a program to extract string from the list if the string is starts with consonent"""
# l=['kavya','mani','egg']
# print([i for i in l  if i[0] not in 'aeiouAEIOU' ])

"""Write a  program to print the given output"""
# l=['python','hello','php','ruby','aws']
# print([i[::-1] if len(i)%2==0 else len(i) for i in l])

"""I/p:- l1=['dora','bujji','chutkii]
         l2=['python','da','ds']"""
"""o/p:- [('dora','python'),('dora','da'),('dora','ds'),
         ('bujji','python'),('bujji','da'),('bujji','ds'),
         ('chutkii','python'),('chutkii','da'),('chutkii','ds')]"""
l1=['dora','bujji','chutkii']
l2=['python','da','ds']
print([[i,j] for i in l1 for j in l2])
