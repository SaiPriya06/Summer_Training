'''ip:
"MMFFMFFMFMFMFFMMFFMMF"
op: M=F 0
M>F m
F>M f'''

s=input()
c,d=0,0
for i in s:
    if i=="M":
        c=c+1
    else:
        d=d+1
if(c==d):
    print(1)
elif(c>d):
    print("m")
else:
    print("f")
    
    
s=input()
c=0
for i in s:
    if i=="M":
        c=c+1
    else:
        c=c-1
if c==0:
    print(1)
elif(c<0):
    print("f")
else:
    print("m")
        