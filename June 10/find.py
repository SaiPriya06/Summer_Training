def fun(i,j,k,t):
    if(k==len(s)):
        return 1
    if(i<0 or j<0 or i>=n or j>=n or a[i][j]!=s[k]):
        return
    if(a[i][j]==s[k]):
        a[i][j]=0
    t=fun(i+1,j,k+1,t)
    t=fun(i-1,j,k+1,t)
    t=fun(i,j-1,k+1,t)
    t=fun(i,j+1,k+1,t)
    return t
for i in range(n):
    for j in range(n):
        if(a[i][j]==s[0]):
            fun(i,j,1,0)
            if(c==1):
                print("yes")
                break
if(c==0):
    print("no")
        