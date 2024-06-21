a=input()
d=[0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(all(d))