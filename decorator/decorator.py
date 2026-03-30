import time
startingtime=time.time()
for i in range(1,11):
    print(i,end="")
endingtime=time.time()
print('time-taken:',endingtime-startingtime)

import time
st=time.time()
def time(func):
    def inner(*args,**kwargs):
        print(' hie Everyone')
        func(*args,**kwargs)
        print("em chestunaru")
    return inner
@time
def msg():
    print("I am kavya using the decorator",st)
msg()
