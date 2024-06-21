'''
ip:
5
0 1 0 0 1
1 0 0 1 1
0 0 0 0 0
1 0 0 0 0
1 0 0 0 1

all 1s are land, 0s are water
'''
def fun(i,j,n,a):
    if(i<0 or i>=n or j>=n or j<0 or a[i][j]!=1):
        return
    a[i][j]='0'
    b=1
    b+=fun(i-1,j,n,a)
    b+=fun(i,j-1,n,a)
    b+=fun(i+1,j,n,a)
    b+=fun(i,j+1,n,a)
    return b

a=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
n=5
m=0
d=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i][j]==1:
            m=m+1
            g=fun(i,j,n,a)
            d=max(g,d)
print(m)
print(d)