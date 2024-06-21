'''ip:122 op:131
ip:24 op:33
ip:7654 op:7667
ip:1234 op:1331
ip:1112  op:1221
ip:56472  op:56565
ip:76583   op:76667'''
def rev_num(num,rev=0):
    if num==0:
        return rev
    else:
        return rev_num(num//10,rev*10+num%10)
def is_pal(num): 
    rev_n=rev_num(num)
    return num==rev_n
def next_palindrome(num):
    num += 1
    while not is_pal(num):
        num += 1
    return num
num=int(input())
if is_pal(num):
    print(num,"is palindrome")
else:
    print(num,"is not palindrome")
next_pal = next_palindrome(num)
print("next palindrome is",next_pal)