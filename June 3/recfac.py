def fa(x):
    if x==1:
        return 1
    return x*fa(x-1)
a=fa(3)
print(a)