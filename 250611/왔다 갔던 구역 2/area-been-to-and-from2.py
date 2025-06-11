n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.


blocks = [0] * 2000
offset = 1000
point = 0


for i in range(n) :

    if dir[i] == 'R' :
        a = x[i] + 1 +offset
        for j in range(point,a) :
            blocks[j] += 1
    else :
        a = x[i] -1 + offset
        for j in range(a,point,-1) :
            blocks[j] += 1


result = max(blocks)
print(result)   



