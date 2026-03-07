def outer():
    global x
    x+=10
    print(x)
x=10
outer()
print(x)
x+=1
print(x)