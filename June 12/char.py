'''ip:"hello:5438,car:214,book:8799,apple:2187"
op:oaxp'''
a=input()
res=""
b=a.split(",")
for i in b:
    c=i.split(":")
    l=len(c[0])
    if str(l) in c[1]:
        res=res+c[0][-1]
    else:
        for i in range(l-1,0,-1):
            if str(i) in c[1]:
                res=res+c[0][i-1]
                break
        else:
            res=res+'x'
print(res)