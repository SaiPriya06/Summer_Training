'''ip
0 1 1 1 0 1
0 1 0 1 0 0
1 0 0 1 0 0
0 0 0 1 1 1
1 1 0 0 0 1
1 1 1 0 1 0

1->trees 0->empty lands
fired on pos 4,6
if tree fires and becomes empty, makes all horizontal, vertical trees to be fired

for pos 4,6,  remaining will be 8
op 8'''

def fun(i,j,n,a):
    if(i<0 or i>=n or j>=n or j<0 or a[i][j]!=1):
        return 
    if a[i][j]==1:
        a[i][j]=2
    fun(i-1,j,n,a)
    fun(i,j-1,n,a)
    fun(i+1,j,n,a)
    fun(i,j+1,n,a)
    return
#invisible return
a=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
fun(3,5,5,a)
c=0
for i in range(5):
    for j in range(5):
        if(a[i][j]==1):
            print(a[i][j],end=" ")
            c+=1
    print()
print(c)