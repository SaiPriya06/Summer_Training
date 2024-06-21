n=[]
s1=input()
s2=input()
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    n.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if(s1[i-1]==s2[j-1]):
            n[i][j]=n[i-1][j-1]+1
        else:
            n[i][j]=max(n[i][j]-1,n[i-1][j])
print(n[len(s1)][len(s2)])
s=""
u=len(s1)
v=len(s2)
while u!=0 and v!=0:
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    elif(n[u-1][v] > n[u][v - 1]):
        u -= 1
    else:
        v -= 1
s=s[::-1]
print(s)