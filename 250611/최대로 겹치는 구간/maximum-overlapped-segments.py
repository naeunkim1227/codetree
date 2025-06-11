# offset = 100
# max_n = 150

# n = int(input())
# segments = [tuple(map(int, input().split())) for _ in range(n)]

# blocks = [0] * (max_n +1)

# for a,b in segments :
    # a,b = a + offset, b + offset
    # for i in range(a,b) :
        # blocks[i] += 1


# print(max(blocks))

OFFSET = 100
MAX_R = 200

# 변수 선언 및 입력
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
checked = [0] * (MAX_R + 1)

for x1, x2 in segments:
    # OFFSET을 더해줍니다.
    x1, x2 = x1 + OFFSET, x2 + OFFSET
    
    # 구간을 칠해줍니다.
    # 구간 단위로 진행하는 문제이므로
    # x2에 등호가 들어가지 않음에 유의합니다.
    for i in range(x1, x2):
        checked[i] += 1

# 최댓값을 구합니다.
max_num = max(checked)
print(max_num)



