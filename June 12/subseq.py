'''
ip:
[4,9,8,2,14,3,5,6]
op:
(4,8,9,2,14,3,5,6)

(4,2,8,9,14,3,5,6)

(4,2,8,9,14,3,5,6)

(4,2,8,3,5,9,14,6)

(4,2,8,3,5,6,9,14)
'''
#1
a=[4,9,8,2,14,3,5,6]
for i in range(len(a)-2):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
    if a[i]>a[i+2]:
        a[i],a[i+2]=a[i+2],a[i]
    if a[i+1]>a[i+2]:
        a[i+1],a[i+2]=a[i+2],a[i+1]
print(a)

#2
a=[4,9,8,2,14,3,5,6]
for i in range(len(a)-2):
    s=a[i]+a[i+1]+a[i+2]
    a[i]=min(a[i],a[i+1],a[i+2])
    a[i+2]=min(a[i],a[i+1],a[i+2])
    a[i+1]=s-min(a[i],a[i+1],a[i+2])-max(a[i],a[i+1],a[i+2])
print(a)
    
print(a)

  
    
    