'''ip
khoor
3
op
hello'''
 
s=input()
n=int(input())
m=n%26
a=""
for char in s:
   shifted=ord(char)-m
   if shifted<ord('a'):
       shifted+=26
   a+=chr(shifted)
print(a)    
        
        
       