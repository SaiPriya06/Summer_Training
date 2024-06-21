'''ip:
[4,8,14,22,36,68]
given numbers are non prime num in increasing order
largest prime between range
op:[7,13,19,31,67]
sum(nums)'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
a=[14,16,20,22]
l=[]
for i in range(len(a)-1):
    m=0
    c=0
    for j in range(a[i],a[i+1]):
        if is_prime(j):
            c=j
    m=max(c,m)
    l.append(m)
print(l)
print(sum(l))
    