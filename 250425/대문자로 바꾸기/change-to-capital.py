a,b = 5,3
arr_2d = [
    list(map(str, input().split()))
    for _ in range(5)
]


for i in range(a) :
    for j in range(b) :
        arr_2d[i][j] = chr(ord(arr_2d[i][j]) + ord('A') - ord('a'))       
        print(arr_2d[i][j], end =" ")
    print()