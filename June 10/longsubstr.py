'''
ip: "abfgresagtyuiofde"
op:  7,9,12'''
a=input()
d={}
s=""
m=0
i=0
while(i<len(a)):
    while(i<len(a)):
        if a[i] not in s:
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i=i+1
    i=d[a[i]]+1
print(m)

#2
def long_substring(s):
    cs=set()
    left=0
    m=0
    for i in range(len(s)):
        while s[i] in cs:
            cs.remove(s[left])
            left+=1
        cs.add(s[i])
        m=max(m,i-left+1)
    return m
s=input()
print(long_substring(s))
    