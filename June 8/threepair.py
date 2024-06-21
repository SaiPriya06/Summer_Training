l="school"
l1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            s=l[i]+l[j]+l[k]
            l1.append(s)
print(l1)