'''
ip:[2,3,5,6] coin 11 value
op : yes '''

def fun(l,n):
    l1=[0]*(n+1)
    l1[0]=1
    for i in l:
        for j in range(1,n+1):
            if j<i:
                j=l1[i]
            elif j>=i:
                k=j-i
                l1[j]=max(l1[j],l1[k])
    return l1[n]        
            
l=[2,3,5,6]
n=16
m=fun(l,n)
if m==1:
    print("yes")
else:
    print("no")