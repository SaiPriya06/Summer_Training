o=input()
s=input()
l=[]
for i in range(len(s)):
    m=o.index(s[i])
    l.append(m)
y=sorted(l)
c=''
for i in y:
    c=c+o[i]
print(c)
#nlogn ,n*26
#n*26 is more time
#2
n=int(input())
while(n):
    a=input()
    c=input()
    k=""
    for i in a:
        if i in c:
            k=k+(i*c.count(i))
    print(k)
    n=n-1