#min cost
def fun(d,s,l,e,c,m):
    l.append(s)
    if s==e:
        if (c<m):
            m=c
        l.pop()
        return m
    for i,j in d[s]:
        if i not in l:
            m=fun(d,i,l,e,c,m)
    l.pop()
    return m
d={5:[(7,1),(3,3)],7:[(5,1),(4,3),(3,2)],4:[(7,3),(8,4),(2,3)],8:[(3,5),(4,4),(2,6)],3:[(5,3),(7,2),(8,5)],2:[(4,3),(8,6)]}
l=[]
print(fun(d,5,l,2,99999))


