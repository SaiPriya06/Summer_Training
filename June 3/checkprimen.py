''' 537=6 op 538
538=7 op 538'''
n=int(input())
m=n
s=0
while(n):
    c=n%10
    s=s+c
    n=n//10
t=0
if len(str(abs(s)))>1:
    d=s%10
    t=t+d
    s=s//10
s1=str(s)
b=s1[0]
b=int(b)
sum=t+b
k=sum
v=0
for i in range(2,sum):
    if(sum%i==0):
        v=1
if(v!=1):        
    print("prime",m)
else:
    while(1):
        e=0
        for i in range(2,(sum//2)+1):
            if (sum%i==0):
                e=e+1
                break
        if(e==0):
            break
        else:
            sum=sum+1
    f=sum-k
    print("need",f,"to become prime",m+f)
    