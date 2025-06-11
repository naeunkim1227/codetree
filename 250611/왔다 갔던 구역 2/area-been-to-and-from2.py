n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.


blocks = [0] * 30

point = 0

for i in range(n) :
    if dir[i] == 'R' :
        for j in range(point,x[i]+1) :
            blocks[j] += 1
    else :
        for j in range(x[i]-1,point,-1) :
            blocks[j] += 1


result = max(blocks)
print(result)   



