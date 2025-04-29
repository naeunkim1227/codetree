arr1 = [
    list(map(int,input().split()))
    for _ in range(3)
]
input()

arr2 = [
    list(map(int,input().split()))
    for _ in range(3)
]

arr3 = [
    [0 for _ in range(3)]
    for _ in range(3)
]
for i in range(3) :
    for j in range(3) : 
        arr3[i][j] = arr1[i][j] * arr2[i][j]

for elem in arr3 :
    for row in elem :
        print(row, end =" ")
    print()


