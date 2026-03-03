"""Write a program given a string of words create a dictionary where words will be the key and value will be the length of the word but it should not start  with a  word vowel letter"""
# s='ello world this is python programming'
# d={}
# for i in s.split():
#     if i[0]  in 'aeiouAEIOU':
#         continue                
#     d[i]=len(i)
# print(d)
"""Write a program to print first n palindrome but the palindrome should not divisible by 11 by using continue statement"""
n=int(input('enter the number:'))
count=0
i=1
while count<n:
    if str(i)==str(i)[::-1]:
        if i%11==0:
            i+=1
            continue
        print(i)
        count+=1
    i+=1
    
    


