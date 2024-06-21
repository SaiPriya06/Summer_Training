'''
ip:
5 3 2 7 8 4
m t w t f s
pen

buy or sell on m,s
sell after buy
max profit

op:
6'''
l=list(map(int,input().split(" ")))
d=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i] < l[j] and l[j]-l[i] >d):
            d=l[j]-l[i]
print(d)