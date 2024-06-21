def fun(d,s,l):
    l.append(s)
    for i in d[s]:
        if i not in l:
            fun(d,i,l)
    return 
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
fun(d,5,l)
print(l)