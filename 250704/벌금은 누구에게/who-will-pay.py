N, M, K = map(int, input().split())

MAX_N = 100

student = [0] * (N + 1)
b_person = [
    int(input())
    for _ in range(M)
]

target = 0
for t in b_person :
    student[t] += 1
    
    if student[t] >= K :
        target = t
        break


print(target)
    

