d = {5:[7,3],3:[5,7,8],7:[5,4],4:[2,7,8],8:[2,3,4],2:[4,8]}
print("BFS:")
visited = set()
q = []
for i in d:
    if i not in visited:
        visited.add(i)
        q.append(i)
    while(q):
        node = q.pop(0)
        print(node,end=" ")
        for n in d[node]:
            if n not in visited:
                visited.add(n)
                q.append(n)
print("\nVisited:",visited)