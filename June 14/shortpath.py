g={5:[(3,1),(1,2),(6,3)],1:[(5,2),(2,1)]}
def fun(x):
    d={5:999,1:9999,3:9999,6:9999,2:9999}
    d[x]=0
    vi=[]
    q=[x]
    while(q):
        m=99999
        for i in q:
            if d[i]<m:
                m=d[i]
                x=i
        for i in g[x]:
            if i[0] not in vi:
                q.append(i[0])
                if d[i[0]]>[i]+d[x]:
                    d[i[0]]=i[1]+d[x]
        vi.append(x)
        q.remove(x)
    return d
fun(5)