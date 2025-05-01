n = 5
answer = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n) :
    answer[0][i] = 1


for i in range(1,n) :
    for j in range(n) :
        if j - 1 >= 0 :
            answer[i][j] = answer[i-1][j] + answer[i][j-1] 
        else :
            answer[i][j] = answer[i-1][j]



for row in answer :
    for elem in row :
        print(elem, end = " ")
    print()