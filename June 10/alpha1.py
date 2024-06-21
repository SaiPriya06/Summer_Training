c=input()
#1
d=0
for i in range(97,123):
    if chr(i) in c:
        d=d+1
if d==26:
    print("yes")
else:
    print("no")

#2
for i in range(97,123):
    if chr(i) not in c:
        print("no")
        break
else:
    print("yes")
    
#3
d=[]
for i in c:
    if i not in d:
        d.append(i)
m=len(d)
if m==27:
    print("yes")
else:
    print("no")