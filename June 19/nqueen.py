def Nqueen(board,r,f):
    if r==len(board):
        return True
    for c in range(len(board)):
        if issafe(board,r,c):
            board[r][c]="1"
            f=f+1
            if Nqueen(board,r+1,f):
                return True
            board[r][c]='0'
    
def issafe(board,r,c):
    for i in range(r):
        if board[i][c]=="1":
            return False
    i,j=r,c
    while i>=0 and j<len(board):
        if board[i][j]=="1":
            return False
        i=i-1
        j=j+1
    i,j=r,c
    while i>=0 and j>=0:
        if board[i][j]=="1":
            return False
        i=i-1
        j=j-1
    return True
n=int(input("enter number of queens:"))
board=[["0" for i in range(n)] for j in range(n)]
f=0
if Nqueen(board,0,f):
    for i in board:
        print("".join(i))
        
    print(f)
else:
    print(False)