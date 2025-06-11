n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.


blocks = [0] * (100)

for a,b in segments :
    for i in range(a,b) :
        blocks[i] += 1


print(max(blocks))