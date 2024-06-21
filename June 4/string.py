'''ip
3
xyz
pqr
abc

"yraxpazr"
op: yes'''

'''ip
4
abcd
xyze
pqrw
stuv

"cyptdzsayq"
op: no'''
n=int(input())
m=[]
f=0
for i in range(n):
    m.append(list(input()))
s=input()
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        print("no")
        break
else:
    print("yes")
    
'''xyz
pqr
abc

"yraxpazr"
op: no

xyz
pqr
abc

"yraxpbzqc"
op: yes



''' 
    
n=int(input())
m=[]
f=0
for i in range(n):
    m.append(list(input()))
s=input()
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        print("no")
        f=1
        break
    else:
        m[i].remove(s[i])
if f==0:
    print("yes")
           
    