N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

cnt = 1
max_cnt = cnt
for i in range(N) :
    if i >= 0 and (arr[i] * arr[i-1]> 0) :
        cnt += 1    
    else :
        cnt = 1


    if max_cnt <= cnt :
        max_cnt = cnt


print(max_cnt)