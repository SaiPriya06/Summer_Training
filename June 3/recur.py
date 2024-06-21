def fun(x):
    if(x==6):
        return
    print(x)
    fun(x+1)
    print(x)
fun(1)
print("hi")
'''in loop it is break;in function it is return'''
#recursion is like spring where if we at end ,come to start thn should go back steps all
def fun(x):
    print("hi")
    return 100
print(fun(10))


def fun(x):
    print("hi")
print(fun(10))

def fun(x):
    if(x==6):
        return 500
    print(x)
    fun(x+1)
    print(x)
print(fun(1))

def fun(x):
    if(x==6):
        return 500
    print(x)
    fun(x+1)
    print(x)
    return 100
print(fun(1))

def fun(x):
    if(x==6):
        return 500
    print(x)
    k=fun(x+1)
    print(x)
    return k
print(fun(1))