#reverse the string and check palindrome or not
def fun(x,re):
    if(x==0):
        return re
    re=re*10+(x%10)
    return fun(x//10,re)
n=int(input())
if(n==fun(n,0)):
    print("palindrome")
else:
    print("no")