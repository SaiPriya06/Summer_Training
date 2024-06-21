'''
ip:[1,2,3,4,1,2,3,1,2]
op:[[1 2 3 4],[1 2 3],[1 2]]
ip: [2,3,1,3,4,3,2]
op: [[2 3 1 4],[3 2],[3]]
ip: [4,5,2,1]
op: [[4 5 2 1]]
'''
#normal
l=[1,2,3,4,1,2,3,1,2]
m=[]
c=0
while(c!=len(l)):
    l1=[]
    for i in range(len(l)):
        if (not str(l[i]).isalpha()):
            if l[i] not in l1:
                c=c+1
                l1.append(l[i])
                l[i]='a'
    m.append(l1)
print(m)

#dictionaries
a=[1,2,3,4,1,2,3,1,2]
d={}
m=[]
c=0
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
c=0
while(c!=len(a)):
    r=[]
    for i in d:
        if(d[i]!=0):
            d[i]=d[i]-1
            c=c+1
            r.append(i)
    m.append(r)
print(m)
    