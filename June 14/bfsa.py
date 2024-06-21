def bfs(d, n):
    vi = []  
    q = [n]  
    while q:
        node = q.pop(0)  
        if node not in vi:
            vi.append(node) 
            print(node)  
            for neighbor in d[node]:
                if neighbor not in q and neighbor not in vi:
                    q.append(neighbor)
d = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}
bfs(d, 5)