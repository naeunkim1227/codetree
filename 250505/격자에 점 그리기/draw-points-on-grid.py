n,m = tuple(map(int,input().split()))

arr = [[0 for _ in range(n)] for _ in range(n)]



val = 1
for i in range(m) :
    a,b = tuple(map(int,input().split()))
    arr[a-1][b-1] = val
    val += 1


for row in arr : 
    for elem in row :
        print(elem, end= " ")
    print()