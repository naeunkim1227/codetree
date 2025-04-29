n,m = list(map(int,input().split()))


arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]



num = 0
for i in range(n):
    for j in range(m):
        num += 1
        arr_2d[i][j] += num

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()