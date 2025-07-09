# n = int(input())
# moves = [tuple(input().split()) for _ in range(n)]
# dir = [move[0] for move in moves]
# dist = [int(move[1]) for move in moves]

# Please write your code here.



n = int(input())

point = [0,0]

for i in range(n) : 
    a,b = tuple(input().split())
    if a == 'W' : 
      point[1] -=  int(b)  
    elif a == 'S' :
        point[0] -= int(b)
    elif a  == 'N' :
        point[0] += int(b) 
    elif a == 'E' :
        point[1] += int(b)


print(point[1], point[0])

