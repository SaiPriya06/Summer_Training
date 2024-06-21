#all paths,weights
def fun(d,s,l,w):
    l.append(s)
    if s==2:
        print(l)
        print("cost=",sum(w))
        l.pop()
        if w:
            w.pop()
        return 
    for i,j in d[s]:
        if i not in l:
            w.append(j)
            fun(d,i,l,w)
    l.pop()
    if w:
        w.pop()
d={5:[(7,1),(3,3)],7:[(5,1),(4,3),(3,2)],4:[(7,3),(8,4),(2,3)],8:[(3,5),(4,4),(2,6)],3:[(5,3),(7,2),(8,5)],2:[(4,3),(8,6)]}
l=[]
w=[]
fun(d,5,l,w)

