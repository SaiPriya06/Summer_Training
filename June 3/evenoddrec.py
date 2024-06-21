'''a=[3,8,5,4,3]
b=[5,0,9,3,2]
op
[12,17]'''
def fun(x,s,t):
    if x==len(a):
        return [s,t]
    if a[x]%2==0:
        s=s+a[x]
    if b[x]%2!=0:
        t=t+b[x]
    return fun(x+1,s,t)
        
a=[3,8,5,4,3]
b=[5,0,9,3,2]
x,y=fun(0,0,0)
print(x,y)