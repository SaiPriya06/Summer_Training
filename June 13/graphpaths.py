def fun(d,s,l,e):
    l.append(s)
    if s==e:
        print(l)
        l.pop()
        return 
    for i in d[s]:
        if i not in l:
            fun(d,i,l,e)
    l.pop()
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
s=5
e=2
fun(d,5,l,e)
