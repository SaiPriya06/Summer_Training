def fun(x,s):
    if(x==len(a)):
        return s
    s=s+a[x]
    k=fun(x+1,s)
    return k
a=[7,8,9,1]
print(fun(0,0))