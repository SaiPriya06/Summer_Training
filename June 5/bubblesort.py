'''7 3 9 2 1 5
'''
#optimised
a=[2,3,6,8,10,11]
c=0
for i in range(len(a)-1):
    f=0
    for j in range(len(a)-1-i):
        if(a[j]>a[j+1]):
            f=1
            a[j],a[j+1]=a[j+1],a[j]
        c=c+1
    if(f==0):
        break
print(a,c)
#normal
a=[2,3,6,8,10,11]
c=0
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
        c=c+1
print(a,c)
            