''' 537=6 op 538
538=7 op 538'''
def add(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s
def pnp(x):
    if(n in [2,3,5,7]):
        return n
    else:
        return n+1
n=int(input())
m=n
if(n<10):
    print(pnp(n))
else:
    while(1):
        n=add(n)
        if(n<10):
            break
    print(m+pnp(n)-n)
    