offset = 100
max_n = 150

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

blocks = [0] * (max_n +1)

for a,b in segments :
    a,b = a + offset, b + offset
    for i in range(a,b) :
        blocks[i] += 1


print(max(blocks))