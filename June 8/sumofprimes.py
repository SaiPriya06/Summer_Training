'''12
sum of 2 primes: 5,7'''
n=int(input())
def is_prime(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1
for i in range(1,(n//2)+1):
    if(is_prime(i)) and is_prime(n-i):
        print("yes")
        break
else:
    print("no")
    
        
    
