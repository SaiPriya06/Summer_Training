x = int(input())  
q = []
for _ in range(x):
    query = input().strip().split(' ')
    q.append((int(query[0]), query[1]))
d = {} 
for query in q:
    qv = query[0]
    word = query[1]
    if qv == 1:
        d[word] = True
    elif qv == 2:
        if word in d:
            print("True")
        else:
            print("False")
    elif qv == 3:
        found = False
        for key in d:
            if key.startswith(word):
                found = True
                break
        print(found)
    elif qv == 4:
        del d[word]
        print(d)