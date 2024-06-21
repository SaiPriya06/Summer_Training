#169 leetcode
'''[3,8,2,3,3,8,3] op:3'''
a=[3,8,1,1,5,8,1]
max=0
for i in a:
    if(a.count(i) >=max):
        max=a.count(i)
        l=i
print(l)

a=[2,2,1,1,1,2,2]
c=1
p=a[0]
for i in range(1,len(a)):
    if(a[i]==p):
        c=c+1
    else:
        if(c!=0):
            c=c-1
        if(c==0):
            c=c+1
            p=a[i]
print(p)
    