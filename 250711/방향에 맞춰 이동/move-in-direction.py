# n = int(input())
# moves = [tuple(input().split()) for _ in range(n)]
# dir = [move[0] for move in moves]
# dist = [int(move[1]) for move in moves]

# Please write your code here.



n = int(input())

dx,dy = [0,-1,0,1], [1,0,-1,0]
pX, pY = 0,0

for i in range(n) : 
    a,b = tuple(input().split())
    b = int(b)
    if a == 'W' : 
        move = 1
    elif a == 'S' :
        move = 2
    elif a  == 'N' :
        move = 0
    elif a == 'E' :
        move = 3

    pX += dx[move] * b
    pY += dy[move] * b


print(pX, pY)



