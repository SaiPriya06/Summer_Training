'''ip
xyzabcdefklmnopqefgh
op
7'''
a=input()
c=1
l=1
for i in range(1,len(a)):
    if (ord(a[i])==ord(a[i-1])+1):
        l+=1
    else:
        c=max(c,l)
        l=1
c=max(c,l)
print(c)