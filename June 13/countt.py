#count
def fun(d,s,l,e,c):
    l.append(s)
    if s==e:
        c=c+1
        l.pop()
        return c 
    for i in d[s]:
        if i not in l:
            c=fun(d,i,l,e,c)
    l.pop()
    return c
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
s=5
e=2
c=0
print(fun(d,s,l,e,c))