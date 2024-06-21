'''
ip: [3,5,9,6,8,10] -> heights sun mrng and evng
op: 3 in mrng nd 1 in evng'''

l=[3,4,5,10,4,3]
m=1
e=1
for i in range(len(l)):
    if l[i]<l[i+1]:
        m=m+1
    else:
        break
for i in range(-1,-len(l)-1, -1):
    if l[i]<l[i-1]:
        e=e+1
    else:
        break
print(m)
print(e)
        
        