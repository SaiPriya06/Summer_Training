'''leet**co*de
op lecde '''
s=input()
m=[]
for i in s:
    if i!="*":
        m.append(i)
    else:
        m.pop()
print(''.join(m))