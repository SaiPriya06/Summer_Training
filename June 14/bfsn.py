def bfs(d,n):
    vi=[]
    q=[n]
    while(q):
        for i in d[q[0]]:
            if (i[0] not in q and i[0] not in vi):
                q.apppend(i[0])
            vi.append(q.pop(0))
            print(vi[-1])
    
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
bfs(d,5)