import math
a=5
b=10
c=math.gcd(a,b)
if c==1:
    print("coprime")
else:
    print("no")
    
for i in range(2,(max(a,b)//2)+1):
    if(a%i==0) and (b%i==0):
        print("not coprime")
        break
else:
    print("coprime")