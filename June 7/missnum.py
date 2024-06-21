#268 leetcode
'''ip
7
0 5 3 6 7 2 1
op:
4'''
n=7
a=[0,5,3,6,7,2,1]
for i in range(n+1):
    if i not in a:
        print(i)
        break
    
n=7
a=[0,5,3,6,7,2,1]
b=sum(a)
n=(n*(n+1))//2
print(n-b)